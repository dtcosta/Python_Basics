{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-12 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-13 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "#import modules for use\n",
    "\n",
    "import csv\n",
    "import os\n",
    " \n",
    "#set the path\n",
    "file = os.path.join ('..', 'PyBank','budget_data.csv')\n",
    " \n",
    "#create lists to store the data\n",
    "dates = []\n",
    "profits = []\n",
    "changes =[]\n",
    "\n",
    "#open csv using path\n",
    "with open (file, newline = \"\") as csvfile:\n",
    "    readcsv = csv.reader(csvfile, delimiter = ',')\n",
    "    csv_header = next(csvfile)\n",
    "     \n",
    "#place the data into lists\n",
    "    for row in readcsv:\n",
    "        dates.append(row[0])\n",
    "        profits.append(int(row[1]))\n",
    "         \n",
    "#count the number of months\n",
    "month_count = len(months)\n",
    "     \n",
    "#set variables \n",
    "x = 1\n",
    "y = 0\n",
    "     \n",
    "#average change place holder\n",
    "average_change = (profits[1]-profits[0])\n",
    "          \n",
    "#calculate month to month change and place into a list\n",
    "for month in range(month_count-1):\n",
    "        average_change = (profits[x] - profits[y])\n",
    "        changes.append(int(average_change))\n",
    "        x+=1\n",
    "        y+=1\n",
    "        \n",
    "#calcuate the average monthly change and round it    \n",
    "average_month_change = round(sum(changes)/(month_count -1),2)\n",
    " \n",
    "#find the min and max change\n",
    "min_change = min(changes)\n",
    "max_change = max(changes)\n",
    " \n",
    "#return the index to find the positions in the list\n",
    "change_i_min = changes.index(min_change)\n",
    "change_i_max = changes.index(max_change)\n",
    "     \n",
    "#find the months for the min and max changes\n",
    "min_change_month = dates[change_i_min + 1]\n",
    "max_change_month = dates[change_i_max + 1]\n",
    "\n",
    "    \n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------\")\n",
    "print(f\"Total Months: {len(dates)}\")\n",
    "print(f\"Total: ${sum(profits)}\")\n",
    "print(f\"Average Change: ${average_month_change}\")\n",
    "print(f\"Greatest Increase in Profits: {max_change_month} (${max_change})\")\n",
    "print(f\"Greatest Decrease in Profits: {min_change_month} (${min_change})\")\n",
    "\n",
    "#write the output to a text file\n",
    "fin_analysis = open(\"Financial_Analysis.txt\",\"w\")\n",
    " \n",
    "fin_analysis.write(\"Financial Analysis\\n\")\n",
    "fin_analysis.write(\"----------------------------\\n\")\n",
    "fin_analysis.write(f\"Total Months: {len(dates)}\\n\")\n",
    "fin_analysis.write(f\"Total: ${sum(net_total)}\\n\")\n",
    "fin_analysis.write(f\"Average Change: {average_month_change}\\n\")\n",
    "fin_analysis.write(f\"Greatest Increase in Profits: {max_chng_month} (${max_change})\\n\")\n",
    "fin_analysis.write(f\"Greatest Decrease in Profits: {min_chng_month} (${min_change})\\n\")\n",
    "  \n",
    "fin_analysis.close() \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
