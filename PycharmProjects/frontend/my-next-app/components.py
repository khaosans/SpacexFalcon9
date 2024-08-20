import tkinter as tk
from chakraui import ChakraUI

class JobCard(ChakraUI.Card):
    def __init__(self, job_data):
        super().__init__()
        self.job_data = job_data
        self.children = [
            ChakraUI.Text(label="Job ID:", value=self.job_data["id"]),
            ChakraUI.Text(label="Job Status:", value=self.job_data["status"])
        ]

class StatusIndicator(ChakraUI.Indicator):
    def __init__(self, status):
        super().__init__()
        self.status = status
        self.children = [
            ChakraUI.Text(label="Status:", value=status)
        ]

class Chart(ChakraUI.Chart):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.children = [
            ChakraUI.LineChart(data=self.data)
        ]
