#!/bin/bash
#===========================================================#
#File Name:			tester.sh
#Author:			Pedro Cumino
#Email:				pedro.cumino@av.it.pt
#Creation Date:		Thu  2 Jan 18:49:52 2025
#Last Modified:		Thu  2 Jan 18:49:54 2025
#Description:
#Args:
#Usage:
#===========================================================#

echo '';
echo 'expense-tracker.py add --description "Lunch" --amount 20';
python3 expense-tracker.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

echo '';
echo 'expense-tracker.py add --description "Dinner" --amount 10';
python3 expense-tracker.py add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

echo '';
echo 'expense-tracker.py list';
python3 expense-tracker.py list
# ID  Date       Description  Amount
# 1   2024-01-01  Lunch        $20
# 2   2024-01-01  Dinner       $10

echo '';
echo 'expense-tracker.py summary';
python3 expense-tracker.py summary
# Total expenses: $30

echo '';
echo 'expense-tracker.py delete --id 2';
python3 expense-tracker.py delete --id 2
# Expense deleted successfully

echo '';
echo 'expense-tracker.py summary';
python3 expense-tracker.py summary
# Total expenses: $20

echo '';
echo 'expense-tracker.py summary --month 1';
python3 expense-tracker.py summary --month 1
# Total expenses for January: $20