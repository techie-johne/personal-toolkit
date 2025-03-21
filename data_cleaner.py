#!/usr/bin/env python3
"""
Data Cleaner Script
------------------
Cleans and formats various data files for analysis.
Supports CSV, TSV, and Excel files.
"""
import pandas as pd
import argparse
import os
import re
import sys
import numpy as np
from datetime import datetime

class DataCleaner:
    def __init__(self, input_file, output_file=None):
        self.input_file = input_file
        
        # Set default output name if not provided
        if output_file:
            self.output_file = output_file
        else:
            file_name, file_ext = os.path.splitext(input_file)
            self.output_file = f"{file_name}_cleaned{file_ext}"
        
        self.df = None
        self.file_type = self._detect_file_type()
    
    def _detect_file_type(self):
        """Detect the file type based on extension"""
        _, file_ext = os.path.splitext(self.input_file)
        
        if file_ext.lower() == '.csv':
            return 'csv'
        elif file_ext.lower() == '.tsv':
            return 'tsv'
        elif file_ext.lower() in ['.xls', '.xlsx']:
            return 'excel'
        else:
            raise ValueError(f"Unsupported file type: {file_ext}")
    
    def load_data(self):
        """Load data from the input file"""
        try:
            if self.file_type == 'csv':
                self.df = pd.read_csv(self.input_file)
            elif self.file_type == 'tsv':
                self.df = pd.read_csv(self.input_file, sep='\t')
            elif self.file_type == 'excel':
                self.df = pd.read_excel(self.input_file)
            
            print(f"Loaded data with {self.df.shape[0]} rows and {self.df.shape[1]} columns")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def clean_column_names(self):
        """Clean and standardize column names"""
        if self.df is None:
            return False
        
        # Convert to lowercase, replace spaces with underscores
        self.df.columns = [re.sub(r'[^\w\s]', '', col).strip().lower().replace(' ', '_') for col in self.df.columns]
        
        # Remove duplicate column names by adding numbers
        seen = {}
        new_columns = []
        
        for col in self.df.columns:
            if col in seen:
                seen[col] += 1
                new_columns.append(f"{col}_{seen[col]}")
            else:
                seen[col] = 0
                new_columns.append(col)
        
        self.df.columns = new_columns
        print("Column names cleaned and standardized")
        return True
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        if self.df is None:
            return False
        
        original_count = self.df.shape[0]
        self.df = self.df.drop_duplicates()
        removed_count = original_count - self.df.shape[0]
        
        print(f"Removed {removed_count} duplicate rows")
        return True
    
    def handle_missing_values(self, strategy='drop'):
        """Handle missing values in the dataset"""
        if self.df is None:
            return False
        
        # Count missing values before
        missing_before = self.df.isna().sum().sum()
        
        if strategy == 'drop':
            # Drop rows with any missing values
            self.df = self.df.dropna()
        elif strategy == 'fill_mean':
            # Fill numeric columns with mean
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                self.df[col] = self.df[col].fillna(self.df[col].mean())
        elif strategy == 'fill_mode':
            # Fill categorical columns with mode
            categorical_cols = self.df.select_dtypes(exclude=[np.number]).columns
            for col in categorical_cols:
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0] if not self.df[col].mode().empty else "")
        elif strategy == 'fill_zero':
            # Fill missing values with zeros
            self.df = self.df.fillna(0)
        elif strategy == 'fill_empty':
            # Fill missing values with empty string
            self.df = self.df.fillna('')
        
        # Count missing values after
        missing_after = self.df.isna().sum().sum()
        print(f"Handled {missing_before - missing_after} missing values using strategy: {strategy}")
        return True
    
    def convert_data_types(self):
        """Convert columns to appropriate data types"""
        if self.df is None:
            return False
        
        for col in self.df.columns:
            # Try to convert to numeric
            try:
                # Check if it looks like a number
                if self.df[col].dtype == 'object' and self.df[col].str.match(r'^-?\d+\.?\d*$').all():
                    self.df[col] = pd.to_numeric(self.df[col])
            except:
                pass
            
            # Try to convert to datetime
            try:
                if self.df[col].dtype == 'object':
                    # Check if it looks like a date
                    date_sample = self.df[col].dropna().iloc[0] if not self.df[col].dropna().empty else ""
                    if re.match(r'\d{1,4}[-/]\d{1,2}[-/]\d{1,4}', str(date_sample)):
                        self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
            except:
                pass
        
        print("Converted columns to appropriate data types")
        return True
    
    def save_data(self):
        """Save the cleaned data to the output file"""
        if self.df is None:
            return False
        
        try:
            if self.file_type == 'csv':
                self.df.to_csv(self.output_file, index=False)
            elif self.file_type == 'tsv':
                self.df.to_csv(self.output_file, sep='\t', index=False)
            elif self.file_type == 'excel':
                self.df.to_excel(self.output_file, index=False)
            
            print(f"Cleaned data saved to {self.output_file}")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def get_data_summary(self):
        """Get a summary of the data"""
        if self.df is None:
            return "No data loaded"
        
        summary = []
        summary.append(f"Data Shape: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        summary.append(f"Column Names: {', '.join(self.df.columns)}")
        
        # Data types
        type_counts = self.df.dtypes.value_counts().to_dict()
        type_summary = ", ".join([f"{count} {dtype}" for dtype, count in type_counts.items()])
        summary.append(f"Data Types: {type_summary}")
        
        # Missing values
        missing = self.df.isna().sum().sum()
        summary.append(f"Missing Values: {missing}")
        
        return "\n".join(summary)

def main():
    parser = argparse.ArgumentParser(description="Clean and format data files")
    parser.add_argument("input_file", help="Input file to clean (CSV, TSV, Excel)")
    parser.add_argument("-o", "--output", help="Output file name (default: original_cleaned.ext)")
    parser.add_argument("-m", "--missing", choices=["drop", "fill_mean", "fill_mode", "fill_zero", "fill_empty"], 
                        default="drop", help="Strategy for handling missing values")
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file {args.input_file} does not exist")
        sys.exit(1)
    
    # Create data cleaner
    cleaner = DataCleaner(args.input_file, args.output)
    
    # Process data
    if cleaner.load_data():
        print("\nData Summary Before Cleaning:")
        print(cleaner.get_data_summary())
        
        cleaner.clean_column_names()
        cleaner.remove_duplicates()
        cleaner.handle_missing_values(args.missing)
        cleaner.convert_data_types()
        
        print("\nData Summary After Cleaning:")
        print(cleaner.get_data_summary())
        
        cleaner.save_data()
    
if __name__ == "__main__":
    main()
