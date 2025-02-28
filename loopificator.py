# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import logging
import os
import tkinter as tk
from tkinter import simpledialog

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging
log_file_path = os.path.join(script_dir, "loopificator_log.txt")
logging.basicConfig(
    filename=log_file_path,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def process_gcode(input_file):
    
    logging.info("Starting G-code processing")
    logging.info(f"Input file: {input_file}")

    # Read the input G-code
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    loops = int(simpledialog.askstring(title="How many loops?",
                                  prompt="How many times do you want to loop this print?:"))
    
    logging.info(f"Looping file {loops} times")