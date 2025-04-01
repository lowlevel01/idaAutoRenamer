import idaapi
import ida_name
import ida_funcs
import json
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog

class AutoRenamerPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "Rename globals or functions using JSON mapping"
    help = "Loads a JSON file with addresses and names"
    wanted_name = "AutoRenamer"
    wanted_hotkey = ""

    def init(self):
        print("[AutoRenamer] Plugin initialized.")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        # Ask user whether to rename globals or functions
        choices = ["Global Variables", "Functions"]
        choice, ok = QInputDialog.getItem(None, "Select Rename Mode", "Choose what to rename:", choices, 0, False)
        if not ok:
            print("[AutoRenamer] Operation canceled.")
            return

        json_path, _ = QFileDialog.getOpenFileName(None, "Select JSON File", "", "JSON Files (*.json)")
        if not json_path:
            print("[AutoRenamer] No file selected, exiting.")
            return

        try:
            with open(json_path, "r") as f:
                rename_data = json.load(f)
        except Exception as e:
            print(f"[AutoRenamer] Failed to load JSON: {e}")
            return

        if choice == "Global Variables":
            success_count = self.rename_globals(rename_data)
            print(f"[AutoRenamer] Renamed {success_count}/{len(rename_data)} global variables.")
        elif choice == "Functions":
            success_count = self.rename_globals(rename_data)
            print(f"[AutoRenamer] Renamed {success_count}/{len(rename_data)} functions.")

    def rename_globals(self, name_to_addr_dict):
        success_count = 0
        for addr_str, new_name in name_to_addr_dict.items():
            try:
                addr = int(addr_str, 16)
                if ida_name.set_name(addr, new_name):
                    print(f"[AutoRenamer] Renamed {hex(addr)} -> {new_name}")
                    success_count += 1
                else:
                    print(f"[AutoRenamer] Failed to rename {hex(addr)}")
            except ValueError:
                print(f"[AutoRenamer] Invalid address format: {addr_str}")

        return success_count

   

    def term(self):
        print("[AutoRenamer] Plugin terminated.")


def PLUGIN_ENTRY():
    return AutoRenamerPlugin()
