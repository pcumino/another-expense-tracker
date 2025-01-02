#!/usr/bin/env python3

#===========================================================#
#File Name:			expense-tracker.py
#Author:			Pedro Cumino
#Email:				pedro.cumino@av.it.pt
#Creation Date:		Thu  2 Jan 18:46:11 2025
#Last Modified:		Thu  2 Jan 18:46:15 2025
#Description:
#Args:
#Usage:
#===========================================================#

import os
import csv
from datetime import datetime

CSV_FILE = 'data.csv'

def add_expense(description, amount):
	try:
		with open(CSV_FILE, 'a', newline='') as csvfile:
			fieldnames = ['ID', 'Date', 'Description', 'Amount']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			
			# Read the current data to determine the next ID
			try:
				with open(CSV_FILE, 'r') as readfile:
					reader = csv.DictReader(readfile)
					rows = list(reader)
					next_id = int(rows[-1]['ID']) + 1 if rows else 1
			except FileNotFoundError:
				next_id = 1
			
			writer.writerow({'ID': next_id, 'Date': datetime.now().strftime('%Y-%m-%d'), 'Description': description, 'Amount': amount})
			print(f"Expense added successfully (ID: {next_id})")
	except Exception as e:
		print(f"Error adding expense: {e}")

def list_expenses():
	try:
		with open(CSV_FILE, 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			print(f"{'ID':<4} {'Date':<10} {'Description':<12} {'Amount':<6}")
			for row in reader:
				print(f"{row['ID']:<4} {row['Date']:<10} {row['Description']:<12} ${row['Amount']:<6}")
	except FileNotFoundError:
		print("No expenses file found.")
	except Exception as e:
		print(f"Error listing expenses: {e}")

def summary(month=None):
	try:
		with open(CSV_FILE, 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			total = 0
			for row in reader:
				if month:
					if datetime.strptime(row['Date'], '%Y-%m-%d').month == int(month):
						total += float(row['Amount'])
				else:
					total += float(row['Amount'])
			if month:
				month_name = datetime(1900, int(month), 1).strftime('%B')
				print(f"Total expenses for {month_name}: $ {total:>5.2f}")
			else:
				print(f"Total expenses: ${total}")
	except FileNotFoundError:
		print("No expenses file found.")
	except Exception as e:
		print(f"Error summarizing expenses: {e}")

def delete_expense(expense_id):
	try:
		rows = []
		with open(CSV_FILE, 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			rows = list(reader)
		
		with open(CSV_FILE, 'w', newline='') as csvfile:
			fieldnames = ['ID', 'Date', 'Description', 'Amount']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for row in rows:
				if row['ID'] == expense_id:
					continue
				writer.writerow(row)
			print("Expense deleted successfully")
	except FileNotFoundError:
		print("No expenses file found.")
	except Exception as e:
		print(f"Error deleting expense: {e}")

def main(args):
	try:
		if not os.path.isfile(CSV_FILE):
			with open(CSV_FILE, 'w') as csvfile:
				fieldnames = ['ID', 'Date', 'Description', 'Amount']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
		
		if args[0] == 'add':
			description = args[args.index('--description') + 1]
			amount = args[args.index('--amount') + 1]
			add_expense(description, amount)
		elif args[0] == 'list':
			list_expenses()
		elif args[0] == 'summary':
			if '--month' in args:
				month = args[args.index('--month') + 1]
				summary(month)
			else:
				summary()
		elif args[0] == 'delete':
			expense_id = args[args.index('--id') + 1]
			delete_expense(expense_id)
		else:
			print("Invalid command")
	except Exception as e:
		print('Error while running the app.\n', e)
		print('\t',args)

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])