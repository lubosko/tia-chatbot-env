# Online and diagnostic tools


---

## Status LEDs

The CPU and the I/O modules use LEDs to provide information about the operating state of the CPU and status of the devices.

## Status LEDs on a CPU

The CPU provides the following status indicators:

- STOP/RUN

  - Solid yellow indicates STOP mode
  - Solid green indicates RUN mode
  - Flashing (alternating green and yellow) indicates that the CPU is in the STARTUP operating state
- ERROR

  - Flashing red indicates an error, such as an internal error in the CPU, an error with the memory card, or a configuration error (mismatched modules)
  - Flashing red for three seconds indicates an error that is not ongoing. An example is if the real time clock (RTC) resets to the default time due to a power loss.
  - Defective state:

    - Solid red indicates defective hardware

    - All LEDs flash if the firmware detects a defect
- MAINT (Maintenance) flashes whenever you insert a memory card. Power cycle the CPU. The CPU then changes to STOP mode. After the CPU has changed to STOP mode, perform one of the following functions to initiate the evaluation of the memory card:

  - Change the CPU to RUN mode
  - Perform a memory reset (MRES)
  - Power-cycle the CPU

You can also use the [LED instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ReE4~wr~aTSnqnI4HIHUPQ?section=Xc1dc7201ea3090cc904d16f3d719a62c) to determine the status of the LEDs.

Table 1. Status LEDs for a CPU

| **Description** | **STOP/RUN Yellow / Green** | **ERROR Red** | **MAINT Yellow** |
| --- | --- | --- | --- |
| Power is off | Off | Off | Off |
| Startup, self-test, or firmware update | Flashing  (alternating yellow and green) | - | Off |
| Stop mode | On (yellow) | - | - |
| Run mode | On (green) | - | - |
| Remove the memory card | On (yellow) | - | Flashing |
| Error | On (either yellow or green) | Flashing | - |
| Maintenance requested   - Forced I/O - Battery replacement required (if battery board installed) | On (either yellow or green) | - | On |
| [Defective hardware](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/D3ncDXPvDQwB5X55bn6S5Q?section=Xd27dc1879185ff01ac374cff1c10ae10) | On (yellow) | On | Off |
| LED test or [defective CPU firmware](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/D3ncDXPvDQwB5X55bn6S5Q?section=Xd27dc1879185ff01ac374cff1c10ae10) | Flashing  (alternating yellow and green) | Flashing | Flashing |
| [Unknown or incompatible version of CPU configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/D3ncDXPvDQwB5X55bn6S5Q?section=Xd27dc1879185ff01ac374cff1c10ae10) | On (yellow) | Flashing | Flashing |

The CPU and each digital signal module (SM) provide an I/O Channel LED for each of the digital inputs and outputs. The I/O Channel (green) turns on or off to indicate the state of the individual input or output.

## Status LEDs on a Signal Module (SM) and a Signal Board (SB)

In addition, each digital SM provides a DIAG LED that indicates the status of the module:

- Green indicates that the module is operational
- Red indicates that the module is defective or non-operational

Each analog SM provides an I/O Channel LED for each of the analog inputs and outputs.

- Green indicates that the channel has been configured and is active
- Red indicates an error condition of the individual analog input or output

In addition, each analog SM provides a DIAG LED that indicates the status of the module:

- Green indicates that the module is operational
- Red indicates that the module is defective or non-operational

The SM detects the presence or absence of power to the module (field-side power, if required).

Table 2. Status LEDs for a signal module (SM)

| **Description** | **DIAG**  **(Red / Green)** | **I/O Channel**  **(Red / Green)** |
| --- | --- | --- |
| Field-side power is off \* | Flashing red | Flashing red |
| Not configured or update in progress | Flashing green | Off |
| Module configured with no errors | On (green) | On (green) |
| Error condition | Flashing red | - |
| I/O error (with diagnostics enabled) | Flashing red | Flashing red |
| I/O error (with diagnostics disabled) | On (green) | On (green) |

\* Status is only supported on analog signal modules.

Each analog SB provides an I/O Channel LED for each of the analog inputs and outputs.

Table 3. Status LEDs for a signal board (SB)

| **Description** | **I/O Channel**  **(Red / Green)** |
| --- | --- |
| Not configured or update in progress | Off |
| Board configured with no errors | On (green) |
| I/O error (with diagnostics enabled) | Flashing red |
| I/O error (with diagnostics disabled) | On (green) |

## Status LEDs for communication on the CPU

The CPU also provides two LEDs that indicate the status of the PROFINET communications. Open the bottom terminal block cover to view the PROFINET LEDs.

- Link (green) turns on to indicate a successful connection
- Rx/Tx (yellow) turns on to indicate transmission activity

## See also

[Resetting to factory settings](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ousE3DGfufW3uTupUTcVWA?section=X491b26087c13e566b0ce80df762d767a)

[Transfer card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_r3864TbweY1WO3Qq1W15A?section=Xc4ab69c3c6e689fe4b088be084919ea9)

[Setting or deleting the password for protection of confidential PLC configuration data](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/TanNmrtmqi3RdpZATLIxkg?section=X428ad9a0212de5508369e0d124d4f606)

[Protection of confidential PLC configuration data](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/weZr~222uiVd9iOtUdI3Ug?section=X28ad57bb3d4f1e3452505460378b64b3)

[Program card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Nduy3t80KgsTMsXV7FGmJA?section=Xce5159a8eea1c3dd262707ee37775108)

[Analog module diagnostics](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7VXjwbA0KrKWzQsy2cOWEQ?section=X0872110a250064ca057b30ce5179fe74)

---

## Analog module diagnostics

Analog modules have multiple diagnostics depending on the module and channel type. You can separately enable or disable these diagnostics for each module and channel by using the TIA portal under the projects device configuration/general properties of the module.

Power supply errors are reported as follows:

| **Power supply error** | **Error reported** |
| --- | --- |
| Analog module with a power supply diagnostic error reports: | Overflow: 32767 for all input channels |
| Missing power supply diagnostic, if enabled for output modules |

You can enable these diagnostics separately by channel and type for each channel. See the table below:

| **Channel type** | **Error reported** |
| --- | --- |
| Voltage input | Overflow: 32767 |
| Underflow: -32768 |
| Current input (0 to 20 mA) | Overflow: 32767 |
| Underflow: -32768 |
| Current input (4 to 20 mA) (for < 1.185 mA input) | Broken wire: 32767 |
| Overflow: 32767 |
| Voltage output (for > 0.5 V output) | Short circuit diagnostic, if enabled |
| Current output (for > 1.0 mA output) | Open circuit diagnostic, if enabled |
| RTD input | Broken wire: 32767 |
| Overflow: 32767 |
| Underflow: -32768 |
| Resistor input | Broken wire: 32767 |
| Overflow: 32767 |
| Thermocouple input | Broken wire: 32767 |
| Overflow: 32767 |
| Underflow: -32768 |

An analog input module with a diagnostic error on any channel reports 32767 or -32768 on that channel even if the diagnostics is not enabled. Analog input channels report 32767 when deactivated.

Analog input modules can have diagnostic errors on more than one channel at a time (multiple errors). When this occurs, only the first error is reported to the CPU. After the first error is reported, no additional errors are reported until the cause of the first error is cleared in the module. After the first error is cleared, the second error is then reported if the error condition still exists.

---

## CPU error behavior

## "Unknown or incompatible version of CPU configuration" error

The diagnostics buffer can report an "Unknown or incompatible version of CPU configuration" error, which can occur in one of the following ways:

- Attempting to load an invalid project, for example, an S7-1200 V3.0 program to an S7-1200 V4.x CPU
- Attempting to download a project with different [protection of confidential PLC configuration data](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/weZr~222uiVd9iOtUdI3Ug?section=X28ad57bb3d4f1e3452505460378b64b3) between the CPU and the project

If you reached this state by using an invalid version [transfer card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_r3864TbweY1WO3Qq1W15A?section=Xc4ab69c3c6e689fe4b088be084919ea9), follow these steps to recover:

1. Remove the transfer card.
2. Perform a STOP to RUN transition.
3. Reset the memory (MRES) or cycle power.

If you reach this state by using an invalid project on a [program card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Nduy3t80KgsTMsXV7FGmJA?section=Xce5159a8eea1c3dd262707ee37775108), [reset the CPU to factory settings](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ousE3DGfufW3uTupUTcVWA?section=X491b26087c13e566b0ce80df762d767a) using the "Format memory card" option .

If your reach this state from a mismatch between the CPU and the project for the protection of confidential PLC configuration data, use the [Online & Diagnostics tools](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/TanNmrtmqi3RdpZATLIxkg?section=X428ad9a0212de5508369e0d124d4f606) to set the online CPU's password for protection of confidential PLC configuration data to the password in the project, or delete it from the online CPU.

After you recover the CPU from the error condition, you can download a valid program.

## S7-1200 behavior following a fatal error

If the CPU firmware detects a fatal error it attempts a defect-mode restart, and if successful, signals the defective mode by continually flashing the STOP/RUN, ERROR and MAINT LEDs. The user program and hardware configuration are not loaded following the defect-mode restart.

If the CPU successfully completes the defect-mode restart, the CPU performs these actions:

- Sets the CPU and signal board outputs to 0
- Sets the outputs of central rack signal modules and distributed I/O to the selection for "Reaction to CPU STOP" in the device configuration of the digital outputs of the module

If the defect-mode restart fails, (for example, due to a hardware fault), the STOP and ERROR LEDs are ON and the MAINT LED is OFF.

Warning:

**Operation in defect state cannot be guaranteed**

Control devices can fail in an unsafe condition, resulting in unexpected operation of controlled equipment.

Use an emergency stop function, electromechanical overrides or other redundant safeguards that are independent of the PLC.

Such unexpected operations can result in death or serious injury to personnel, and/or damage to equipment.

---

## Going online and connecting to a CPU

You can establish an online connection between the programming device and CPU for loading programs and project engineering data as well as for activities such as the following:

- Testing user programs
- Displaying and changing the [operating mode of the CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/CB4j5VIhmfmLF3~VMrf0jA?section=X44a4220e7c79942bdbb600fa55378f00)
- Displaying and [setting the date and time of day of the CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/0Dh5hSOjz~rjENkx14i3~A?section=X1d59b0d62162534872b6bba8f83c27fe)
- Displaying the module information
- [Comparing and synchronizing](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ks8PJnYJhx6SKkzGOW71eQ?section=Xaf663d9b33268dc62d29c185ccb969fa) offline to online program blocks
- Uploading and downloading program blocks
- Displaying diagnostics and the [diagnostics buffer](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/zgO3cAw23NoyQvWyioETiA?section=X6a76e5153ca5c4e6e920c34ff9f602eb)
- Using a [watch table](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/tMuiw4v~nC0nL5Cct3iSIA?section=X90bf632571d39a1a74ca597a82c3ff78) to test the user program by monitoring and modifying values
- Using a force table to [force values in the CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/MMPEQKto9BGqLK8oQmtL4w?section=X48f8d87b97dba32c4d5ed30b6e3ac3bd)
- [Resetting the CPU to factory settings](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ousE3DGfufW3uTupUTcVWA?section=X491b26087c13e566b0ce80df762d767a)

To establish an online connection to a configured CPU, click the CPU from the Project Navigation tree and click the "Go online" button from the Project View: [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFIAAAAXCAIAAAAX248TAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAlwSFlzAAASdAAAEnQB3mYfeAAAAlZJREFUWEftmD9IAlEcx2tzaHBocBVcDlqEhm7soCHBobGgIaRBxEGkwaElxMGhocFBxCGwQbDh4ByCcwlss81Rx8bGG3/9fl1dz7v3nnd2XsIlhxz3573fh+/3fX9Ptyevk60YfhA7hsdWDJnJ4EGx3ysq9EvQUIO+uFHPB8O2KtoXcyZp6OZGkQQqRoY9fTFQW/awmceZxKxZGOhGoJk26mEh9vS5R9o+VekYlkCvOjrPmqWBbpqjccQk2HDsGZ2TlQvgY09HvcFOgpbxQ87qatDSrKYKNypcZSeZJOosYXa64co1iV78Pa0zMgcbvU06z00iL2eRGb6ZoUjYklXNVhZilWGJLMNGka1hFe5zMDeMPeXtPA3XKlQUuFTgNG2rzRVEwim3gPeuPZR9/adWj8m5j7EbMKFxvDfI28Oq1dbgjjQ3dhOzo5TNDHnCFqktwpZbQATmXcncK5LHJCnAMTlhP5bgVrMaKtSy8DpAt08Pk3CcgsOkH7Vd6q2GvVRkFxXLz+62+cbkq42NCgMMmYsKXCjv/TpqPtlPILPZ7fhUmxu8XkfIbcyy+RTWT6YI1O4WMLTJ2OcKnKTgKDW7LqDm42YdW9f4Rdi6/DN4xeQSRoRNGd5mmPPEDAfkbWRGnSXMTt5yI8qVT6zLRJHmCnCfarORJowbdnpa1chcyeI+jDiZb7Pdkescepde64ALJodWAcrUmcnSuonaYq/6/KbzpTqvtdBwB1/ELiu0366dyfdh4VbwJ6O5I83WNvr9dsTwwX54Rlzc+qb7x47Tn2oxVfsDXJ+ZuV5Z4vUAAAAASUVORK5CYII=)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/3qrOskBjZs8iwQeIDRBpMw-VBkTPlmjVZAl17lebjV9hA)

If this is the first time to go online with this CPU, you must select the type of PG/PC interface and the specific PG/PC interface from the Go Online dialog before establishing an online connection to a CPU found on that interface.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/zqv0trRRIw8V4I1TVlJXQw-VBkTPlmjVZAl17lebjV9hA/content?v=bec9ca8cb02de58e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/zqv0trRRIw8V4I1TVlJXQw-VBkTPlmjVZAl17lebjV9hA)

If the CPU has [protection of confidential PLC configuration data](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/weZr~222uiVd9iOtUdI3Ug?section=X28ad57bb3d4f1e3452505460378b64b3), you might be prompted to trust the CPU. You can display and verify the CPU's certificate and decide whether to trust the CPU online connection or abort the connection.

## Logging on to a CPU

When you go online with the CPU, you must first select one of the following user profiles. If your Anonymous user does not have the necessary permissions, STEP 7 will prompt you to enter an access level password or username and password.

- Log on with access level password - if [access control via access levels](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/boJrawCTV7~GzOYPMsNOtA?section=X6b7b6de0ce1887813501b51c2fcc624a) is enabled for your project, STEP 7 prompts you to enter a password you have configured and downloaded. You are then granted access to the functions and memory areas allowed by the selected level of access protection.
- Local user - you assign a local user with a user name and password in "[Users and Roles](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1)". Enter the configured user name and password to log in.
- Anonymous user - this user is disabled by default; if it is activated under "[Users and Roles](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7nIuqWCd4bYr85ym87r3Cg?section=Xacdebbc7e299aa37867bfd6f048080e1)", you can log in with this user profile.

You then have the rights based on how you logged in. To log off from the online CPU, select the "Online > Delete access rights" menu command.

After connection, the orange color frames indicate an online connection. You can now use the Online & diagnostics tools from the Project tree and the Online tools task card.

## See also

[Downloading in RUN mode](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PPT275Llk_wsnVgNq0TnYg?section=X1a1165b093d3591682068ea01cff3774)

---

## Assigning a name to a PROFINET IO device online

The devices on your PROFINET network must have an assigned name before you can connect with the CPU. Use the "Devices & networks" editor to assign names to your PROFINET devices if the devices have not already been assigned a name or if the name of the device is to be changed.

For each PROFINET IO device, you must assign the same name to that device in both the STEP 7 project and, using the "Online & diagnostics" tool, to the PROFINET IO device configuration memory (for example, an ET200 S interface module configuration memory). If a name is missing or does not match in either location, the PROFINET IO data exchange mode will not run.

Table 1.

|  |  |
| --- | --- |
| 1. In the "Devices & networks" editor, right-click on the required PROFINET IO device, and select "Online & diagnostics". |  |
| 2. In the "Online & diagnostics" dialog, make the following menu selections:   - "Functions" - "Assign PROFINET device name"   Click the "Update list" button to display all of the PROFINET IO devices on the network. |  |
| 3. In the list that is displayed, click the required PROFINET IO device, and click the "Assign name" button to write the name to the PROFINET IO device configuration memory. |  |

---

## Setting the IP address and time of day

You can set the [IP address](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/oacYQyX7UIjTNwr2qIZk_w?section=Xc86058ad710e1c8ad76a2f6658b17a7a)  and time of day in the online CPU. After accessing "Online & diagnostics" from the Project tree for an online CPU, you can display or change the IP address.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/YtAW09e0eti4p49xpetLEQ-VBkTPlmjVZAl17lebjV9hA/content?v=cc5efd5960453fba)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/YtAW09e0eti4p49xpetLEQ-VBkTPlmjVZAl17lebjV9hA)

Note:

The IP address must be assigned in the device in order to set the time of day using the Online and diagnostic interface.

You can also display or set the time and date parameters of the online CPU.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Dx2en2B9jI00WEp2qRLv4Q-VBkTPlmjVZAl17lebjV9hA/content?v=2aa467a7e3e28c0c)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Dx2en2B9jI00WEp2qRLv4Q-VBkTPlmjVZAl17lebjV9hA)

---

## Updating firmware

You can update the firmware of a connected CPU from the STEP 7 online and diagnostics tools, by one of two methods:

- Updating from the CPU in the project
- Updating from the accessible devices in the project tree

Note:

The firmware update process discards any additional data appended to the firmware update file. Appending data to a firmware update file has no effect on the firmware update or the S7-1200 CPU. You cannot append data, for example, to add components.

## Updating the firmware of a CPU in your project

To perform a firmware update, follow these steps:

1. Open the CPU in the Project Tree that corresponds to the connected CPU.
2. Open the Online and Diagnostics view of the connected CPU.
3. Select "Firmware update" from the "Functions" folder.
4. From the "Firmware loader" section, click the Browse button and navigate to the location that contains the firmware update file. This could be a location on your hard drive to which you have downloaded an [S7‑1200](http://support.automation.siemens.com/WW/view/en/34612486/133100) firmware update file from the [Siemens Industry Online Support Web site](http://support.industry.siemens.com).
5. Select a file that is compatible with your module. For a selected file, the table displays the compatible modules.
6. Click the "Run update" button. Follow the dialogs, if necessary, to change the operating mode of your CPU.

STEP 7 displays progress dialogs as it loads the firmware update. When it finishes, it prompts you to start the module with the new firmware.

Note:

If you do not choose to start the module with the new firmware, the previous firmware remains active until you reset the module, for example by cycling power. The new firmware becomes active only after you reset the module.

## Updating the firmware from the accessible devices

To perform a firmware update for one or more accessible devices, follow these steps:

1. Open "Online access" from the project tree.
2. Open the communications interface to which your CPU is connected.
3. Double-click "Update accessible devices" and wait for STEP 7 to display the online devices.
4. Expand the CPU that you want to update and double-click "Online & diagnostics".
5. Expand "Firmware update" from the "Functions" folder. You will see the PLC as well as local modules for the PLC. From either the "PLC" or "Local modules" selection, you can proceed with updating firmware from the "Firmware loader" section as described above.

Note:

The IP address must be assigned in the device in order to update the firmware using the Online & diagnostics.

You can also perform a firmware update by one of the following methods:

- [Using a SIMATIC memory card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/XLe71wDLvkXNxEC28i~Zmw?section=Xba37034bbadf94b220337737383609e3)
- [Using the Web server "Module Information" standard Web page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zkw1i6aTf022QhpONsl5wA?section=X9fd7e004bb711f264161b0cf27efe2e5)
- Using the [SIMATIC Automation Tool](https://support.industry.siemens.com/cs/ww/en/view/98161300)

---

## Setting or deleting the password for protection of confidential PLC configuration data

The "Protection of confidential PLC configuration data" feature allows you to protect each CPU in your project individually. From the [device configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/weZr~222uiVd9iOtUdI3Ug?section=X28ad57bb3d4f1e3452505460378b64b3), you can enable this protection and set a password for the "protection of confidential PLC configuration data". Clients such as TIA Portal and the SIMATIC Automation Tool can only access the confidential data in the PLC through use of the password.

You can also use the [security wizard](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/JBozdBBqBiS6X3H1HpAA5A?section=Xeedbe92d12c70f0e6e9da1973bfd090b) to enable this feature and set the password for the "protection of confidential PLC configuration data".

## Using the online and diagnostics tools

If the password for protection of PLC configuration data in the CPU does not match the one in the project, the CPU cannot go to RUN mode. You must set the correct password for protection of PLC configuration data or delete it for the CPU to go to RUN mode.

When the CPU is [online](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/DD0kYV~aBXliwFCstTwS8Q?section=X697e6c023185521f532da290cbe45678), follow these steps to set or delete the password for "protection of confidential PLC configuration data" that is in the online CPU:

1. Place the CPU in STOP mode.
2. Open the Online & diagnostics tools for your CPU.
3. If the CPU has an existing password for protection of PLC configuration data, reset the PLC as follows:

   - Select "Reset to factory settings" from the Functions menu.
   - Select "Delete password for protection of PLC configuration data".
   - Click "Reset PLC".
4. Select "Set password for protection of PLC configuration data" from the Functions menu.
5. Click "Setup" to set a password or click "Delete" to delete the existing password for protection of confidential PLC configuration data that is in the online CPU. If "Delete" is not available, the online CPU does not have a password for protection of confidential PLC configuration data.

Note:

To set or delete the password for protection of confidential PLC configuration data using the Online & diagnostics tools, the Device configuration must specify "IP address is set directly at the device".

---

## Resetting to factory settings

You can reset an S7-1200 to its original factory settings under the following conditions:

- The CPU has an online connection.
- The CPU is in STOP mode.

  Note:

  If the CPU is in RUN mode and you start the reset operation, you can place it in STOP mode after acknowledging a confirmation prompt.

## Procedure

To reset a CPU to its factory settings, follow these steps:

1. Open the Online & Diagnostics view of the CPU.
2. Select "Reset to factory settings" from the "Functions" folder.
3. Select the "Delete IP address" check box if you want to delete the IP address.
4. Select the "Delete password for protection of confidential PLC configuration data" check box if you want to delete that password. You might want to delete the password for example, if you plan to load a new project to the CPU or [replace the CPU with a new device](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Ea0mk0rOcWTq~9xsZsknJw?section=X422475282e18f995f66fdebf66e7d4cb).
5. Select the "Format memory card" check box if you want to format the memory card that is currently inserted in the online CPU. If you are running your CPU program from the memory card and you want to format the program, select this check box.
6. Click the "Reset PLC" button.
7. Acknowledge the confirmation prompt with "Yes" to confirm that you want to reset the module with your settings.

## Result

The module switches to STOP mode if necessary, and it resets the factory settings. The online CPU performs the following actions:

- Deletes the work memory and retentive data areas
- Deletes the load memory if it is internal load memory; deletes load memory on SIMATIC memory card ONLY if you also selected "Format memory card"
- Sets all parameters and operand areas to their configured values
- Clears the diagnostics buffer
- Resets the time of day
- Deletes the I&M (Identification and Maintenance) data except for I&M0
- Resets the runtime meters if you have not saved the values to a memory card
- Retains or deletes the IP address based on the selection you made. (The MAC address is fixed and is never changed.)If you did not select "Delete IP address", the CPU retains the IP address, subnet mask, and router address (if used) from the settings in your hardware configuration, unless you have modified these values from the user program or another tool, in which case the CPU restores the modified values.
- Deletes the [control data record](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/v6c4hw~HvDGlToNiwAWW7g?section=Xede0597a7a96a33de1dd57e02ebd5437), if present
- Deletes or retains the password for protection of confidential PLC configuration data, depending on your setting
- Formats the memory card if a memory card is installed in the online CPU and you selected the option to format the memory card

---

## Checking a module for defects (saving service data)

## Saving service data

The S7-1200 CPUs allow you to save the service data of a module.

In the event of servicing, the SIEMENS Customer Support requires information about the state of a module of your system for diagnostic purposes. If such a case occurs in your system, Customer Support can ask you to save the service data of the module and send the resulting file to them.

**How to save the service data of a module**

You can save service data of a module in its online and diagnostics view at the following points:

In the "Functions" folder in the "Save service data" group," the "Save service data" group consists of the following areas:

- Online data
- Saving service data

Note:

The IP address must be assigned in the device in order to save the service data of a module.

**"Online data"**

The "Online data" area shows the following data of the module:

- Article number (MLFB)
- Firmware version
- Module name (you configured this while configuring the hardware.)
- Rack
- Slot

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Y2iNjBcmCGyvaMIM~zpGIA-VBkTPlmjVZAl17lebjV9hA/content?v=a81947297bd049ab)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Y2iNjBcmCGyvaMIM~zpGIA-VBkTPlmjVZAl17lebjV9hA)

**"Save service data"**

Proceed as follows to create and save a file with special service data:

1. Select the point in the file system at which you want to save the file:

   - Use the path preset in the "Path" field.
   - Click the three-dot (browse) button. In the dialog that opens specify the desired path and enter the file name.
2. Click the "Save data" button.
3. A status indication for reading the service data is shown. When the service data extraction completes successfully, the Saving Service Data completed successfully screen is shown.

Some things to note:

- Service data can be extracted from the S7-1200 in either RUN or STOP mode. It cannot be read in the Defect/Fatal state.
- If you have programmed a password protection level into the CPU, you must authenticate the password before extracting service data. The password authentication is required for all levels of password, because the service data extraction process includes a data record write.
- The TIA portal supports saving one service data file
- The S7-1200 service data elements contained in the service data file are encrypted.

---

## Formatting a SIMATIC memory card from STEP 7

You can format the memory card in a connected CPU from the STEP 7 online and diagnostic tools. Before you do so, read about the associated [risks](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vigU7rJrF3NUV8Dx9ahVDg?section=Xac2688e7353037b616906099600e725d).

To format the memory card, follow these steps:

1. Ensure the CPU is in STOP mode. Note that if the CPU is in RUN mode and you start a formatting operation, STEP 7 prompts you to allow STEP 7 to put the CPU in STOP mode.
2. Insert a memory card into the connected CPU.
3. Open Online & diagnostics for the connected CPU from either the CPU in the project or from the accessible devices in Online access in the project tree.
4. If the CPU is not online, select "Go online" for the connected CPU.
5. Select "Format memory card" from the "Functions" menu.
6. Click "Format".
7. Confirm the prompt with "Yes".

STEP 7 then formats the memory card and displays a message in the Info window when complete. The CPU is in STOP at the completion of the format operation with the STOP and MAINT lights blinking. You cannot go to RUN mode at this point; you must take one of the following actions:

- Remove the memory card and restart the CPU: If the internal load memory of the CPU contains a program, the CPU starts with the program.
- Restart the CPU without removing the memory card: If the internal load memory of the CPU contains a program, the CPU copies it to the memory card and starts with that program. If the internal load memory has no program, the CPU changes the memory card to a [Program card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Nduy3t80KgsTMsXV7FGmJA?section=Xce5159a8eea1c3dd262707ee37775108) and waits for a download.

Note:

The IP address must be assigned in the device in order to Format a SIMATIC memory card from STEP 7.

## Risks associated with the decommissioning process

S7-1200 CPUs do not support secure erasure of the memory card and internal flash. Therefore, during the decommissioning process, you must securely dispose of the CPU and memory card to prevent the loss of proprietary or confidential information.

Note:

Formatting a memory card has no effect on the contents of internal load memory.

If the CPU was using internal load memory when you inserted the memory card and you did not restart the CPU between inserting the card and executing the format operation, the CPU retains the contents of internal load memory.

---

## CPU operator panel for the online CPU

|  |  |
| --- | --- |
|  | The "CPU operator panel" displays the operating mode (STOP or RUN) of the online CPU. The panel also shows whether the CPU has an error or if values are being forced. |

Use the CPU operating panel of the Online Tools task card to change the operating mode of an online CPU. The Online Tools task card is accessible whenever the CPU is online.

Note:

**The IP address must be assigned in the device in order to use the CPU operator panel.**

---

## Monitoring the cycle time and memory usage

Table 1.

|  |  |  |
| --- | --- | --- |
| You can monitor the cycle time and memory usage of an online CPU.  After connecting to the online CPU, open the Online tools task card to view the following measurements:   - Cycle time - Memory usage | Figure 1. | Figure 2. |
| Figure 3. | | Figure 4. |

Note:

**The IP address must be assigned in the device in order to monitor the cycle time and memory usage.**

---

## Displaying diagnostic events in the CPU

Use the diagnostics buffer to review the recent activity in the CPU. The diagnostics buffer is accessible from "Online & Diagnostics" for an online CPU in the Project tree. It contains the following entries:

- Diagnostic events
- Changes in the CPU operating mode (transitions to STOP or RUN mode)

The first entry contains the latest event. Each entry in the diagnostics buffer contains the date and time the event was logged, and a description. The maximum number of entries is 500.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/wy5W7qGa3McCf6IxrbYQHg-VBkTPlmjVZAl17lebjV9hA/content?v=d3fb8e632016aab8)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/wy5W7qGa3McCf6IxrbYQHg-VBkTPlmjVZAl17lebjV9hA)

Resetting the CPU to the factory settings resets the diagnostics buffer by deleting the entries.

You can also use the [GET DIAG instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/pd0Whq2ORcKU2LgALgpHMw?section=X9867adf4dcc5ca557963ace0f66dbb55) to collect the diagnostic information.

Note:

The IP address must be assigned in the device in order to view the diagnostic events in the CPU.

---

## Comparing offline and online CPUs

You can compare the code blocks in an online CPU with the code blocks in your project. If the code blocks of your project do not match the code blocks of the online CPU, the "Compare" editor allows you to synchronize your project with the online CPU by downloading the code blocks of your project to the CPU, or by deleting blocks from the project that do not exist in the online CPU.

|  |  |  |  |
| --- | --- | --- | --- |
| Figure 1. | Select the CPU in your project.  Use the "Compare Offline/online" command to open the "Compare" editor. (Access the command either from the "Tools" menu or by right-clicking the CPU in your project.) | | |
| Figure 2. | | | Click in the "Action" column for an object to select whether to delete the object, take no action, or download the object to the device. |
| Click the "Synchronize" button to load the code blocks. |
| Figure 3. | | Right-click an object in the "Compare to" column and select "Start detailed comparison" button to show the code blocks side-by-side.  The detailed comparison highlights the differences between the code blocks of online CPU and the code blocks of the CPU in your project. | |

Note:

**Read access required on protected CPU for the Offline/Online compare operations**

For STEP 7, the "HMI access" security level is insufficient to perform the Offline/Online compare operations. You must have "Read access" or "Full access", to do Offline/Online compare operations.

**See also** [Access protection for the CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/boJrawCTV7~GzOYPMsNOtA?section=X6b7b6de0ce1887813501b51c2fcc624a)

---

## Performing an online/offline topology comparison

From the topology overview in STEP 7, you can compare the configured offline topology with the actual online topology.

## Procedure

To find the differences between the configured and the actual topology, follow these steps:

1. Display the topology overview table of the topology view.
2. Click the "Offline/online comparison" button in the toolbar of the topology overview:[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAASCAIAAADQR7l6AAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH3wQeEywH089hEgAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAABVklEQVQ4jWN89eoVAw7gUnf72c0z11ZG4lIAASxofK3wlWwcXOzc/Bw8/KwcXAwMDPZlF398+fjz68dfP75dWxlO2AgpNcNy188MDAwMDH869zAwMDDU+PxhYOBmYODu3M27+9BZVztjNC1MyBz/lpv//v6ZtJfZ1c4YWamrnfGUQzwQKUxXoBjx4cuvjlCmD1//nTp/A00dHimEER61lzhZ/nz8/JWT5U/N0tfIivBIoRjx+dO3pmBOfl7uXR1m7z//RrYNjxQDcnD++fPL280Wyv796+PnrwwMfLilsBnx99dPXtNqCJtHRAlZER4pFCM4Wf/ziir9//fv379/PGy/kRXhkUIx4vA0t1Pnb8Adyc/LTYwUA1rSMjPUQDF//W2cUkiAEZ5HtMKX41KEBtByDcIVPz6/JNIItGSOMOLetoLdh84SaQoyYMST2YkETISV0MEIAC3WtnOQZHN6AAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Lwi37H0XlM9JmG5QV9b76g-VBkTPlmjVZAl17lebjV9hA)

## Result

STEP 7 removes the "Partner station, "Partner interface" and "Cable data" columns in the topology overview table and inserts comparison columns for "Status", and "Action". For each device or port in the topology overview, the Status column displays the comparison status as follows:

| **Icon** | **Meaning** |
| --- | --- |
|  | Differing topology in at least one lower-level component |
|  | Identical topology |
|  | Topology information is only available offline, or device is disabled |
|  | Topology information is only available online |
|  | Differing topology |
|  | Device does not support topology functions |

For each compared port or device, the Action column provides these possible choices:

| **Icon** | **Meaning** |
| --- | --- |
|  | No action possible |
|  | Adopt the online interconnection |

To repeat the comparison, click the [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAUCAIAAADgN5EjAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH3wQeFAIH3Yd+uwAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAACHElEQVQ4jcWUT2gTQRTGvzfZ3WyShogiVqI0tLSG4sH/QpAUtD168GqP4kkKPSgIBVvwIqKC4N2bh9yEoIeUYoNETRuw9lIlIIgxNVGLttmd3U3meUgISZpTPfjdZt785n3vvWGoUqlgTxJ7w/6J1HrWqRfumxW59cfzvHqj3vD71YUzwevT+5vR2w/o3k3uk3PuoZd917AcEiSEECTIsvjl0vb0zGcAN+5I16lnsoXenAuP2ZYQRPHh6vGxreZm/r1ZWA9bFl+d+W6aZh+36SUhHSYSly9+ADA+GosePgBgKonZ+S8bRcXwGESgXnLtowCp4SMlAFPJ05135/K/AqafmQgA7yJtCUEYi1XHR2OdWDyR8/t1YoABJt7tlohIEICmybY2conF5QJTA7AAqzNE7TfUbFqP1U7NPfIJIe7Oel05r1z7GhwYCgXN9CvPNA3D0Non2mLFTJzJFpq3t+a5U5PWjqzVpG07UrrJU28Xlwud2PMMK4au1XrrtCwJMAMAG/SNGJMTXbazK0rXxKF9PyLhUBdpWw4YAkRwbdtc/2RMTrSYVNp9vao03af7aiNDm9HBWBcppcuMhVvO09SAtH25VV9+raxpmq5puqHpumb4rOTZYiQcaje/Vafr1u/PgxjPnhw7f0IGAg4rVkopVoZujxwtX0oUI+HQuZPx/lNpj6RU/lnarP7ebvUjEg5FBw/2jJr+w5/wF1EA5rG7p1e8AAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/P0H2LFNpIkdM3DAaQ1Ct_g-VBkTPlmjVZAl17lebjV9hA) toolbar button on the topology overview.

For additional information on the topology view, the topology overview, and online/offline topology comparisons, refer to the STEP 7 Information System. Also you can find additional information in the [PROFINET with STEP 7 manual](https://support.industry.siemens.com/cs/ww/en/view/49948856).

---

## Monitoring and modifying values in the CPU


---

### Overview of the online monitoring and modification tools

STEP 7 provides online tools for monitoring the CPU:

- You can display or monitor the current values of the tags. The monitoring function does not change the program sequence. It presents you with information about the program sequence and the data of the program in the CPU.
- You can also use other functions to control the sequence and the data of the user program:

  - You can modify the value for the tags in the online CPU to see how the user program responds.
  - You can force a peripheral output (such as Q0.1:P or "Start":P) to a specific value.
  - You can enable outputs in STOP mode.

    Note:

    Always exercise caution when using control functions. These functions can seriously influence the execution of the user/system program.

Table 1. Online capabilities of the STEP 7 editors

| **Editor** | **Monitor** | **Modify** | **Force** |
| --- | --- | --- | --- |
| Watch table | Yes | Yes | No |
| Force table | Yes | No | Yes |
| Program editor | Yes | Yes | No |
| Tag table | Yes | No | No |
| DB editor | Yes | Yes | No |

---

### Going online to monitor the values in the CPU

|  |  |  |
| --- | --- | --- |
| To monitor the tags, you must have an online connection to the CPU. Simply click the "Go online" button in the toolbar. | | |
|  | |  |
|  | When you have connected to the CPU, STEP 7 turns the headers of the work areas orange.  The project tree displays a comparison of the offline project and the online CPU. A green circle means that the CPU and the project are synchronized, meaning that both have the same configuration and user program.  Tag tables show the tags. Watch tables can also show the tags, as well as direct addresses. | |
| Figure 1. | | |

|  |  |
| --- | --- |
|  | To monitor the execution of the user program and to display the values of the tags, click the "Monitor all" button in the toolbar. |
|  | |

The "Monitor value" field shows the value for each tag.

---

### Displaying status in the program editor

You can monitor the status of up to 50 tags in the LAD and FBD program editors. Use the editor bar to display the LAD editor. The editor bar allows you to change the view between the open editors without having to open or close the editors.

In the toolbar of the program editor, click the "Monitoring on/off" button to display the status of your user program.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAUCAIAAAAGHlpnAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH2QoKDSsUuJqlxQAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAAB1ElEQVQ4jWM0TrvMQC7Y3iLOwMDAwsDAMCH2Axn6CxYLQBhMZDsBDlggVGL+6X///v7/9/ffvz///v62MhPNSdGfOP30/sN3/v359fff779/fv37+2vX5gKcRjD8/3/3fMm3b99fv3137/6jmNTNB488+Pfn95tHU+GCXn49zl7d///+zs9x8/c1gRsB9ch/hv+/fv36/OXL589f3719//////4Ou/8Mf5EFGRj+L5yXsmhhZt/ErdhcwcCwbNVpXW3+p89efPv+g+H/PwYGhv///z958uL9x09Pn704c+HN////GRgYZCQEGRj+YzGirli7ofvIv79//v37/e/v76ZqMwYGhgXTA0xsm//++f3v36+/f3/X1fhAFC9dko/FCCV5njn95q/efoZLSIkJMDExblge9+wVIsrFhHlhDsHmETZWFjQ5BgYGJiZGTEF0NXjkbGxsFBQU8OsnYAQDA8Njoc8EDSJghNXdAod7pbcE3uAxiHACP/j1kvP9cr3bGYd4bmM1iAWbLhRgz61XJxbtxGNw4+adFXs2MzAw8HKz8/NyEWvEMeUJllyaN27eWXEZi2aijBB8zIpHM2Ejjhw58uTFezyaiXIFwXQFNQJe/pAHAOOc3TuQoY1/AAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8I6eRLNAFzBDmc3lKGzJIA-VBkTPlmjVZAl17lebjV9hA)

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/XCuU7AUN6SmXEYXg6JqqvA-VBkTPlmjVZAl17lebjV9hA)

The network in the program editor displays power flow in green.

You can also right-click on the instruction or parameter to modify the value for the instruction.

---

### Capturing a snapshot of the online values of a DB for restoring values

You can capture a snapshot of the actual values of data block tags from an online CPU for later use.

Note the following prerequisites:

- You must have an online connection to the CPU.
- You must have the DB open in STEP 7.

## Capturing a snapshot

To capture a snapshot, follow these steps:

1. In the DB editor, click the "Monitor all tags" button: [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAUCAIAAAAGHlpnAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH2QoKDSsUuJqlxQAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAAB1ElEQVQ4jWM0TrvMQC7Y3iLOwMDAwsDAMCH2Axn6CxYLQBhMZDsBDlggVGL+6X///v7/9/ffvz///v62MhPNSdGfOP30/sN3/v359fff779/fv37+2vX5gKcRjD8/3/3fMm3b99fv3137/6jmNTNB488+Pfn95tHU+GCXn49zl7d///+zs9x8/c1gRsB9ch/hv+/fv36/OXL589f3719//////4Ou/8Mf5EFGRj+L5yXsmhhZt/ErdhcwcCwbNVpXW3+p89efPv+g+H/PwYGhv///z958uL9x09Pn704c+HN////GRgYZCQEGRj+YzGirli7ofvIv79//v37/e/v76ZqMwYGhgXTA0xsm//++f3v36+/f3/X1fhAFC9dko/FCCV5njn95q/efoZLSIkJMDExblge9+wVIsrFhHlhDsHmETZWFjQ5BgYGJiZGTEF0NXjkbGxsFBQU8OsnYAQDA8Njoc8EDSJghNXdAod7pbcE3uAxiHACP/j1kvP9cr3bGYd4bmM1iAWbLhRgz61XJxbtxGNw4+adFXs2MzAw8HKz8/NyEWvEMeUJllyaN27eWXEZi2aijBB8zIpHM2Ejjhw58uTFezyaiXIFwXQFNQJe/pAHAOOc3TuQoY1/AAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8I6eRLNAFzBDmc3lKGzJIA-VBkTPlmjVZAl17lebjV9hA) The "Monitor value" column displays the actual data values.
2. Click the [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAASCAIAAAA2bnI+AAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH4AETEAYxvv5kLwAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAABhklEQVQ4jZ2SzStEURjGz5WFjzvmhpGywcbHJDRKSkRGochHFiRFKf+AWLBTlMiCYkehSUpkZTNJbMhkgVkIhXRHDRbumfc597IwmRnN3MHTWZznrV8979sjqarK4sky7ZT82tvUYfgwIS4mL7d+fZThij+Qqa7ucKv0l/6KTNnt/WCMSUH7EQlL5nvuH5wyxjqORyW/ttU8/z131jgSzdM6axyMMXYcaeOmNVeIrGsYn5hc/z0ZTLu54xkabiPQ8qo7wIlz/q5xLfi0jZzYpKEbayt7umE4KovT02VbpmIvzJMtyY+PPvfBactl7eBAU/S0QhdV1WWVVXabzUqEEnv++bm3q33s7MxbXl5EAIs8T4jUdSMrW8nIUkAgwGqVZ2dcPvV1aXHbIsuCEPNCAgJCAIIAEC6ubnv6Gi1pSZ3d9fcPT4CIuSeEEBAgEIEAj8dbUJA7tzCiqs+HRycQJiRABAAEokDg9eXt+uaOa5xzzgOkRyND7fsqmol+XChOb030//Z9AoYCy2SMV7VTAAAAAElFTkSuQmCC)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/A6kOyOJECDTrC5nFMS9xWA-VBkTPlmjVZAl17lebjV9hA) button to capture a snapshot of the actual values and display them in the "Snapshot" column.

You can use this snapshot at a later time to update the actual CPU values or to replace the start values.

## Copying the snapshot values to the CPU

To copy the snapshot values to the actual values of the data block tags in the CPU, click the following button: [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAUCAIAAADgN5EjAAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH4AETEwUzeZvomQAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAABu0lEQVQ4ja2TPWtUQRSGz8zmZneziRgSu1gJio2NYGew0Mom/yNNQPYPRMgvSLGNrf4AwSJCBBWsLKISE2XzpWF1183dZK93Zs7HjMVINuh1idFTHQYenvfAvKrdbsOZRp8N+ydy5Hhrfq5++DRmUYfw80UpqIz6yxfzSzNmmPPN1rhxAwwAQgDj9NrHcjc9GkZmmS9MddRX65s7w8i1t6b1haz1URsCmFx2d/KXz75ZpGF3CvuNjZxI2IpDRitkGZ2g48Is+iTJJIyeSBiFUQjjUnzFwGkNkfPkGC07x2Q9OibkY3J25Rbl+tXc6m9ODIxC6Al9NAt7piBc7Pwff4iYCYWImYRRhIRIhOVPzsGd7DxTTCtMnsl78o3l6ZEStw4KWjEg0+ZK2q8llWmdnAtQQZuxSRXUFr7fhTIsvdAx4I1HtwV170lSqtfrkbx6ZWJ/r3nY2Tpsb/Y77xVtn5/oTk7pawc3311YDaICK0/as04fjzbmF9XJfma57XR7vbSf5cY5KpeT8bFqkpRanXRJLYgpsdFfH1Yb84t3Zq+rUzb76fPX9+29/Qe1iAHAackIA0DE/o78ZX4A8io+t6xluPAAAAAASUVORK5CYII=)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/LjK2VpFUwC6NEPT4N8N6IA-VBkTPlmjVZAl17lebjV9hA)

The online CPU loads the snapshot values into the actual values. The Monitor value column shows the actual values in the CPU. The scan cycle might subsequently change the values in the CPU from the snapshot values, but at the time you make the copy, the CPU loads the snapshot values in a consistent download.

Note:

Be aware that if your snapshot contains state information, timer values, or calculated information, the CPU restores those values as of the time you made the snapshot.

## Copying the snapshot values to the start values

To copy the snapshot values to the start values of the data block tags, click the following button: [![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAASCAIAAAA2bnI+AAAACXBIWXMAABJ0AAASdAHeZh94AAAAB3RJTUUH4AETExQws0uaMwAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAABz0lEQVQ4jZ1Tz0sVURQ+981I8Ax9oghutFqlCyOSFhEaiNBOF2/jwkVEf0L5B5hbtxZIRIskeOamgjI3Ioag4YsQHiqVFcTwdF6M2cw9v1rMkOKbQfBw4cJ37sf3ne9yjOd5cKZy40sElssF/8BlNv97jqMt5+nmlVoul8I0sear5VZLaX0A0MORgT/15ATIpAGAyS99KNfDCaG6x1nEH98jZMpkrm+EO18wCIRZY4RI/X3a+Bi8nk+PMElIFbZ2bKWiSEKWCQVDspYxZMR0O0fjiaiICAuTsBUiZRQmffGUhn9PZTMVhJVImIRJiYRRCHX2ib3w/h4c4sLSerpbFmFWiXVQGJmJn89EF+fGAMAYgI6Tmsl/3nlwjqyQZbSCEduInk2Hl2aKqRMG4wtHbpmVSYiUUBCFUABg/tGm8f/Wn9h5otndNX351pjJ5ZM8LWMkL2el3NdTvN2hAKXRx8dlh/qvJXOOjF5/++ZdY6HTzbcbtxkjCgN/cODX4tpmqa+n2N8Wv05JaOLhVbfBrq7sVnc/B34NFBqbm1pamyYnovsrn0o3euFuRkIAIAKV7a9etYbMqhBH2uA47W0Fx3G+/fROaJoz72f2ipxW/wBI8jDpadLlBgAAAABJRU5ErkJggg==)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/c900VgLnePnIaS8rHxUzsQ-VBkTPlmjVZAl17lebjV9hA)

After you compile the DB and download it to the CPU, the DB uses the new start values when the CPU goes to RUN mode.

## Copying individual snapshot or monitor values to start values

The data block editor also lets you copy individual values and paste them over start values. Simply right-click a value in any value column and select Copy to place it in the Windows clipboard. Then, you can right-click on any start value and select paste to replace that value with the value in the clipboard.

After you compile the DB and download it to the CPU, the DB uses the new start values when the CPU goes to RUN mode.

---

### Using a watch table to monitor and modify values in the CPU


---

#### Watch tables for monitoring the user program

A watch table allows you to perform monitoring and control functions on data points as the CPU executes your program. These data points can be process image (I or Q), M, DB or physical inputs (I\_:P), depending on the monitor or control function. You cannot accurately monitor the physical outputs (Q\_:P) because the monitor function can only display the last value written from Q memory and does not read the actual value from the physical outputs.

The monitoring function does not change the program sequence. It presents you with information about the program sequence and the data of the program in the CPU.

Control functions enable the user to control the sequence and the data of the program. You must exercise caution when using control functions. These functions can seriously influence the execution of the user/system program. The three control functions are Modify, Force and Enable Outputs in STOP.

With the watch table, you can perform the following online functions:

- Monitoring the status of the tags
- Modifying values for the individual tags

You select when to monitor or modify the tag:

- Beginning of scan cycle: Reads or writes the value at the beginning of the scan cycle
- End of scan cycle: Reads or writes the value at the end of the scan cycle
- Switch to stop

|  |  |
| --- | --- |
|  | To create a watch table:   1. Double-click "Add new watch table" to open a new watch table. 2. Enter the tag name to add a tag to the watch table.   The following options are available for monitoring tags:   - Monitor all: This command starts the monitoring of the visible tags in the active watch table. - Monitor now: This command starts the monitoring of the visible tags in the active watch table. The watch table monitors the tags immediately and once only. |

The following options are available for modifying tags:

- "Modify to 0" sets the value of a selected address to "0".
- "Modify to 1" sets the value of a selected address to "1".
- "Modify now" immediately changes the value for the selected addresses for one scan cycle.
- "Modify with trigger" changes the values for the selected addresses.

  This function does not provide feedback to indicate that the selected addresses were actually modified. If feedback of the change is required, use the "Modify now" function.
- "Enable peripheral outputs" disables the command output disable and is available only when the CPU is in STOP mode.

To monitor the tags, you must have an online connection to the CPU.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/tzefKvov~xfUdFhRgk5qUg-VBkTPlmjVZAl17lebjV9hA/content?v=57ae057a7864a187)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/tzefKvov~xfUdFhRgk5qUg-VBkTPlmjVZAl17lebjV9hA)

You use the buttons at the top of the watch table to select the various functions.

Enter the tag name to monitor and select a display format from the dropdown selection. With an online connection to the CPU, click the "Monitor" button to display the actual value of the data point in the "Monitor value" field.

---

#### Using a trigger when monitoring or modifying PLC tags

Triggering determines at what point in the scan cycle the selected address will be monitored or modified.

Table 1. Types of triggers

| **Trigger** | **Description** |
| --- | --- |
| Permanent | Continuously collects the data |
| At scan cycle start | Permanent: Continuously collects the data at the start of the scan cycle, after the CPU reads the inputs |
| Once: Collects the data at the start of the scan cycle, after the CPU reads the inputs |
| At scan cycle end | Permanent: Continuously collects the data at the end of the scan cycle, before the CPU writes the outputs |
| Once: Collects the data once at the end of the scan cycle, before the CPU writes the outputs |
| At transition to STOP | Permanent: Continuously collects data when the CPU transitions to STOP |
| Once: Collects the data once after the CPU transitions to STOP |

For modifying a PLC tag at a given trigger, select either the start or the end of cycle.

- Modifying an output: The best trigger event for modifying an output is at the end of the scan cycle, immediately before the CPU writes the outputs.

  Monitor the value of the outputs at the beginning of the scan cycle to determine what value is written to the physical outputs. Also, monitor the outputs before the CPU writes the values to the physical outputs in order to check program logic and to compare to the actual I/O behavior.
- Modifying an input: The best trigger event for modifying an input is at the start of the cycle, immediately after the CPU reads the inputs and before the user program uses the input values.

  If you suspect values are changing during the scan, you might want to monitor the value of the inputs at the end of the scan cycle to ensure that the value of the input at the end the scan cycle has not changed from the start of the scan cycle. If there is a difference in the values, your user program might be erroneously writing to inputs.

To diagnose why the CPU might have gone to STOP, use the "Transition to STOP" trigger to capture the last process values.

---

#### Enabling outputs in STOP mode

The watch table allows you to write to the outputs when the CPU is in STOP mode. This functionality allows you to check the wiring of the outputs and verify that the wire connected to an output pin initiates a high or low signal to the terminal of the process device to which it is connected.

Warning:

**Risks in writing to physical outputs in STOP mode**

Even though the CPU is in STOP mode, enabling a physical output can activate the process point to which it is connected, possibly resulting in unexpected equipment operation.

Before writing to an output from the watch table, ensure that changing the physical output cannot cause unexpected equipment operation. Always observe safety precautions for your process equipment.

Unexpected equipment operation can cause death or severe personal injury.

You can change the state of the outputs in STOP mode when the outputs are enabled. If the outputs are disabled, you cannot modify the outputs in STOP mode. To enable the modification in STOP mode of the outputs from the watch table, follow these steps:

1. Select the "Expanded mode" menu command from the "Online" menu.
2. Select the "Enable peripheral outputs" option of the "Modify" command of the "Online" menu, or from the context menu after right-clicking the row of the Watch table.

You cannot enable outputs in STOP mode if you have configured distributed I/O. An error is returned when you try to do this.

Setting the CPU to RUN mode disables "Enable peripheral outputs" option.

If any inputs or outputs are forced, the CPU is not allowed to enable outputs while in STOP mode. The force function must first be cancelled.

---

### Forcing values in the CPU


---

#### Using the force table

A force table provides a "force" function that overwrites the value for an input or output point to a specified value for the peripheral input or peripheral output address. The CPU applies this forced value to the input process image prior to the execution of the user program and to the output process image before the outputs are written to the modules.

Note:

The force values are stored in the CPU and not in the force table.

You cannot force an input (or "I" address) or an output (or "Q" address). However, you can force a peripheral input or peripheral output. The force table automatically appends a ":P" to the address (for example: "On":P or "Run":P).

|  |  |
| --- | --- |
|  | |
| In the "Force value" cell, enter the value for the input or output to be forced. You can then use the check box in the "Force" column to enable forcing of the input or output. | |
|  | Use the "Start or replace forcing" button to force the value of the tags in the force table. Click the "Stop forcing" button to reset the value of the tags. |

In the force table, you can monitor the status of the forced value for an input. However, you cannot monitor the forced value of an output.

You can also view the status of the forced value in the program editor.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/XCuU7AUN6SmXEYXg6JqqvA-VBkTPlmjVZAl17lebjV9hA)

Note:

When an input or output is forced in a force table, the force actions become part of the project configuration. If you close STEP 7, the forced elements remain active in the CPU program until they are cleared. To clear these forced elements, you must use STEP 7 to connect with the online CPU and then use the force table to turn off or stop the force function for those elements.

---

#### Operation of the Force function

The CPU allows you to force input and output point(s) by specifying the physical input or output address (I\_:P or Q\_:P) in the force table and then starting the force function.

In the program, reads of physical inputs are overwritten by the forced value. The program uses the forced value in processing. When the program writes a physical output, the output value is overwritten by the force value. The forced value appears at the physical output and is used by the process.

When an input or output is forced in the force table, the force actions become part of the user program. Even though the programming software has been closed, the force selections remain active in the operating CPU program until they are cleared by going online with the programming software and stopping the force function. Programs with forced points loaded on another CPU from a memory card will continue to force the points selected in the program.

If the CPU is executing the user program from a write-protected memory card, you cannot initiate or change the forcing of I/O from a watch table because you cannot override the values in the write-protected user program. Any attempt to force the write-protected values generates an error. If you use a memory card to transfer a user program, any forced elements on that memory card will be transferred to the CPU.

Note:

**Digital I/O points assigned to HSC, PWM, and PTO cannot be forced**

The digital I/O points used by the high-speed counter (HSC), pulse-width modulation (PWM), and pulse-train output (PTO) devices are assigned during device configuration. When digital I/O point addresses are assigned to these devices, the values of the assigned I/O point addresses cannot be modified by the force function of the force table.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/0tOgfgw4n9Df22Joiku0nA-VBkTPlmjVZAl17lebjV9hA/content?v=6c19206e101e9455)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/0tOgfgw4n9Df22Joiku0nA-VBkTPlmjVZAl17lebjV9hA)

|  |  |  |  |
| --- | --- | --- | --- |
| Startup | | RUN | |
| A | The clearing of the I memory area is not affected by the Force function. | ① | While writing Q memory to the physical outputs, the CPU applies the force value as the outputs are updated. |
| B | The initialization of the outputs values is not affected by the Force function. | ② | When reading the physical inputs, the CPU applies the force values just prior to copying the inputs into I memory. |
| C | During the execution of the Startup OBs, the CPU applies the force value when the user program accesses the physical input. | ③ | During the execution of the user program (program cycle OBs), the CPU applies the force value when the user program accesses the physical input or writes the physical output. |
| D | The storing of interrupt events into the queue is not affected. | ④ | Handling of communication requests and self-test diagnostics are not affected by the Force function. |
| E | The enabling of the writing to the outputs is not affected. | ⑤ | The processing of interrupts during any part of the scan cycle is not affected. |

---

## Downloading in RUN mode


---

### Overview

The CPU supports "Download in RUN mode". This capability allows you to download program changes while the program is running.

Warning:

**Risks when downloading in RUN mode**

When you download changes to the CPU in RUN mode, the changes immediately affect process operation. Changing the program in RUN mode can result in unexpected system operation.

Only authorized personnel who understand the effects of RUN mode changes on system operation should perform a download in RUN mode.

Unexpected system operation can cause death or serious injury to personnel, and/or damage to equipment.

The "Download in RUN mode" feature allows you to make changes to a program and download them to your CPU without switching to STOP mode:

- You can make minor changes to your current process without having to shut down (for example, change a parameter value).
- You can debug a program more quickly with this feature (for example, invert the logic for a normally open or normally closed switch).

You can make the following program block and tag changes and download them in RUN mode:

- Create, overwrite, and delete Functions (FC), Function Blocks (FB), and Tag tables.
- Create, delete, and overwrite Data Blocks (DB) and instance data blocks for Function Blocks (FB). You can add to DB structures and download them in RUN mode. The CPU can maintain the values of existing block tags and initialize the new data block tags to their initial values, or the CPU can set all data block tags to initial values, depending on your [configuration settings](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/xTWA~Kd7abSTaU_GtbyKcg?section=X1a56e28207af579e069c03eb6d71ba8e). You cannot download a web server DB (control or fragment) in RUN mode.
- Overwrite Organization Blocks (OB); however, you cannot create or delete OBs.

You can download a maximum number of 20 blocks in RUN mode at one time. If you need to download more than 20 blocks, you must place the CPU in STOP mode.

If you download changes to a running process, you must think through the possible safety consequences to machines and machine operators before you download.

Note:

If the CPU is in RUN mode and program changes have been made, TIA Portal always tries to download in RUN first. If you do not want this to happen, you must put the CPU into STOP.

If the changes made are not supported in "Download in RUN", TIA Portal prompts you that the CPU must go to STOP.

---

### Prerequisites for "Download in RUN mode"

To be able to download your program changes to a CPU that is in RUN mode, you must meet these prerequisites:

- Your program blocks must compile successfully.
- You must have successfully established communication between the CPU and the programming device.

---

### Changing your program in RUN mode

To change the program in RUN mode, you must first ensure that the CPU and program meet the [prerequisites](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/dwOmLCDosoaigROg63V0RA?section=X7b1838c8da8594d5056cbaaff9dab6ba), and then follow these steps:

1. To download your program in RUN mode, select one of the following methods:

   - Select the "Download to device" command from the "Online" menu.
   - Click the "Download to device" button in the toolbar.
   - In the "Project tree", right-click "Program blocks" and select the "Download to device > Software (only changes)" command.

     [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/9cM_JOoHUsXgrPpODRl8eg-VBkTPlmjVZAl17lebjV9hA/content?v=69308bab56a05207)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/9cM_JOoHUsXgrPpODRl8eg-VBkTPlmjVZAl17lebjV9hA)

   If the program compiles successfully, TIA Portal starts to download the program to the CPU.
2. When TIA Portal prompts you to load your program or cancel the operation, click "Load" to download the program to the CPU.

---

### Downloading selected blocks

From the Program blocks folder, you can select a single block or a selection of blocks for downloading.

If you select a single block for downloading, then the only option in the "Action" column is "Consistent download".

You can expand the category line to be sure what blocks are to be loaded. In this example, a small change was made to the offline block, and no other blocks need to be loaded.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/PMey0rtZNPa86wuBWM5~kQ-VBkTPlmjVZAl17lebjV9hA/content?v=21080652533c1762)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/PMey0rtZNPa86wuBWM5~kQ-VBkTPlmjVZAl17lebjV9hA)

In this example, more than one block is needed for downloading.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/rBFll4xnixgg0yLK9W3MQQ-VBkTPlmjVZAl17lebjV9hA/content?v=a7fe533b58c60169)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/rBFll4xnixgg0yLK9W3MQQ-VBkTPlmjVZAl17lebjV9hA)

Note:

You can download a maximum number of 20 blocks in RUN mode at one time. If you need to download more than 20 blocks, you must place the CPU in STOP mode.

If you attempt to download in RUN, but the system detects that this is not possible prior to the actual download, then the Stop modules category line appears in the dialog.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ZfnQmNJFcVkac7XmKwoR1Q-VBkTPlmjVZAl17lebjV9hA/content?v=bbc8cd0695bf5ea2)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ZfnQmNJFcVkac7XmKwoR1Q-VBkTPlmjVZAl17lebjV9hA)

Click the "Load" button, and the "Load results" dialog appears. Click the "Finish" button to complete the download.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/cdO3H~6gUJPwIjGQIK00HQ-VBkTPlmjVZAl17lebjV9hA/content?v=5041dbdd876346ce)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/cdO3H~6gUJPwIjGQIK00HQ-VBkTPlmjVZAl17lebjV9hA)

---

### Downloading a single selected block with a compile error in another block

If you attempt a consistent download with a compile error in another block, then the dialog indicates an error, and the load button is disabled.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/APqzhtGY886AT_ZDItfiag-VBkTPlmjVZAl17lebjV9hA/content?v=aabffda2f93d61cd)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/APqzhtGY886AT_ZDItfiag-VBkTPlmjVZAl17lebjV9hA)

You must correct the compile error in the other block. Then, the "Load" button becomes active.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/19UosI2Gg7BRT_6uqFCUIw-VBkTPlmjVZAl17lebjV9hA/content?v=4e31b92259ad98fb)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/19UosI2Gg7BRT_6uqFCUIw-VBkTPlmjVZAl17lebjV9hA)

---

### Modifying and downloading existing tags in RUN mode

The Download in Run feature allows you to add and modify tags in data blocks and function blocks and then download the changed block to the CPU in RUN mode.

## Download without reinitialization

Each DB and FB has an amount of reserved memory, which you can use for adding tags to the block that you can subsequently download in RUN mode. By default, the initial size of the memory reserve is 100 bytes. You can add additional tags to your data up to the size of the memory reserve and download the extended block to the CPU in RUN mode. You can also increase the memory reserve if you need more memory for additional tags in your block. If you add more tags than the amount of memory you have allocated, you cannot download the extended block to the CPU in RUN mode.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/suYJqqzSn6fYikq732TpoA-VBkTPlmjVZAl17lebjV9hA/content?v=49bb0375414295fe)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/suYJqqzSn6fYikq732TpoA-VBkTPlmjVZAl17lebjV9hA)

The "Download without reinitialization" feature allows you to extend a data block by adding more data block tags and download the extended data block in RUN mode. In this way, you can add tags to a data block and download it without reinitializing your program. The CPU retains the values of the existing data block tags and initializes the newly-added tags to their start values.

To enable this function for an online project with a CPU in RUN mode, follow these steps:

1. From the Program blocks folder in the TIA Portal project tree, right-click the block and select "Properties".
2. Click "Download without reinitialization" and select the "Enable download without reinitialization for retentive tags" checkbox in the block editor to enable the function.
3. Click "OK" on the prompt to confirm your choice.
4. Add tags to the block interface and download the block in RUN mode. You can add and download as many new tags as your memory reserve allows.

If you have added more bytes to your block than you have configured for the memory reserve, TIA Portal displays an error when you attempt to download the block in RUN mode. You must edit the block properties to increase the amount. You cannot delete existing entries or modify the “Memory reserve” of the block while the “Download without reinitialization” function is enabled. To disable the "Download without reinitialization" function, follow these steps:

1. From the Program blocks folder in the TIA Portal project tree, right-click the block and select "Properties".
2. Click "Download without reinitialization" and de-select the "Enable download without reinitialization for retentive tags" checkbox in the block editor to disable the function.
3. Click "OK" on the prompt to confirm your choice.
4. Download the block. On the download dialog, you must select "reinitialize" in order to download the extended block.

The download then reinitializes all existing and new block tags to their start values.

## Downloading retentive block tags

Downloading retentive block tags in RUN mode requires the allocation of a retentive memory reserve. To configure this retentive memory reserve, follow these steps:

1. From the Program blocks folder in the TIA Portal project tree, right-click the block and select "Properties" from the context menu.
2. Select the "Download without reinitialization" property.
3. Select the check box for "Enable download without reinitialization for retentive tags".
4. Configure the number of bytes available for the retentive memory reserve.
5. Click "OK" to save your changes.
6. Add retentive data block tags to the data block and download the data block in RUN mode. You can add and download as many new retentive data block tags as your retentive memory reserve allows.

If you have added more retentive bytes to your data block than you have configured for the retentive memory reserve, TIA Portal displays an error when you attempt to download the block in RUN mode. You can only add retentive block tags up to the retentive memory reserve in order to be able to download them in RUN mode.

When you download the extended retentive block tags, the tags contain their current values.

## Configuring amount of reserved memory for new blocks

The default memory reserve size for new data blocks is 100 bytes. When you create a new block, it has 100 bytes available in reserve. If you want the memory reserve size to be different for new blocks, you can change the setting in the PLC programming settings:

1. From TIA Portal, select the **Options > Settings** menu command.
2. From the Settings dialog, expand "PLC programming" and select "General".
3. In the "Download without reinitialization" section, enter the number of bytes for the memory reserve.

When you create new blocks, TIA Portal uses the memory reserve configuration that you entered for the new blocks.

## Restrictions

The following restrictions apply to editing and downloading blocks in RUN mode:

- Extending the block interface by adding new tags and downloading in RUN mode is only available for [optimized blocks](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/IxCBbripjunRmKx8JqV3ow?section=Xab191af4163631338b11dd99d7c21bbf).
- You cannot change the structure of a block and download the changed block in RUN mode without reinitializing. Adding new members to a [Struct](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/uOQ6o0lY0rg5kmZmnfHF4Q?section=X61bbffbaf60288ca006936d1888a9ffa) tag, changing tag names, array sizes, data types, or retentive status all require that you reinitialize the block if you download it in RUN mode. The only modifications to existing block tags that you can perform and still download the block in RUN mode without reinitialization are changes to start values (data blocks), default values (function blocks) or comments.
- You cannot download more new block tags in RUN mode than the memory reserve can accommodate.
- You cannot download more new retentive block tags in RUN mode than the retentive memory reserve can accommodate.

---

### System reaction if the download process fails

During the initial Download in RUN operation, if a network connection failure occurs, STEP 7 displays the following "Load preview" dialog:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/h_j6z7wy6COZXkZJb0T~3g-VBkTPlmjVZAl17lebjV9hA/content?v=db701dcb584b1a4b)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/h_j6z7wy6COZXkZJb0T~3g-VBkTPlmjVZAl17lebjV9hA)

---

### Considerations when downloading in RUN mode

Before downloading the program in RUN mode, consider the effect of a RUN-mode modification on the operation of the CPU for the following situations:

- If you deleted the control logic for an output, the CPU maintains the last state of the output until the next power cycle or transition to STOP mode.
- If you deleted a high-speed counter or pulse output functions which were running, the high-speed counter or pulse output continues to run until the next power cycle or transition to STOP mode.
- Any logic that is conditional on the state of the first scan bit will not be executed until the next power cycle or transition from STOP to RUN mode. The first scan bit is set only by the transition to RUN mode and is not affected by a download in RUN mode.
- The current values of data blocks (DB) and/or tags can be overwritten.

## Requirements

Before you can download your program in RUN mode, the CPU must support changes in RUN mode, the program must compile with no errors, and the communication between TIA Portal, and the CPU must be error-free.

You can make the following changes in program blocks and tags and download them in RUN mode:

- Create, overwrite, and delete Functions (FC), Function Blocks (FB), and Tag tables.
- Create and delete Data Blocks (DB); however, DB structure changes cannot be overwritten. Initial DB values can be overwritten. You cannot download a Web server DB (control or fragment) in RUN mode.
- Overwrite Organization Blocks (OB); however, you cannot create or delete OBs.

You can download a maximum number of 20 blocks in RUN mode at one time. If you need to download more than 20 blocks, you must place the CPU in STOP mode.

Once you initiate a download, you cannot perform other tasks in TIA Portal until the download completes.

## Instructions that might fail due to "Download in RUN mode"

The following instructions might experience a temporary error when download in RUN mode changes are being activated in the CPU. The error occurs when the instruction is initiated while the CPU is preparing to activate the downloaded changes. During this time, the CPU suspends initiation of user-program access to the Load Memory, while it completes in-progress user program access to Load Memory. This is done so that downloaded changes can be activated consistently.

| **Instruction** | **Response while Activation is Pending** |
| --- | --- |
| DataLogCreate | STATUS = W#16#80C0, ERROR = TRUE |
| DataLogOpen | STATUS = W#16#80C0, ERROR = TRUE |
| DataLogWrite | STATUS = W#16#80C0, ERROR = TRUE |
| DataLogClose | STATUS = W#16#80C0, ERROR = TRUE |
| DataLogNewFile | STATUS = W#16#80C0, ERROR = TRUE |
| DataLogClear | STATUS = W#16#80C0, ERROR = TRUE |
| DataLogDelete | STATUS = W#16#80C0, ERROR = TRUE |
| READ\_DBL | RET\_VAL = W#16#82C0 |
| WRIT\_DBL | RET\_VAL = W#16#82C0 |
| Create\_DB | RET\_VAL = W#16#80C0 |
| Delete\_DB | RET\_VAL = W#16#80C0 |
| RTM | RET\_VAL = 0x80C0 |

In all cases the RLO output from the instruction will be false when the error occurs. The error is temporary. If it occurs, the instruction should be retried later.

If one of the above instructions fails to execute because a download in RUN mode was in process, retry the failed instruction in a subsequent execution of that OB. If you retry the instruction in the same OB execution, it will fail.

---

## Tracing and recording CPU data on trigger conditions

STEP 7 provides trace and logic analyzer functions with which you can configure variables for the PLC to trace and record. You can then upload the recorded trace measurement data to your programming device and use STEP 7 tools to analyze, manage, and graph your data. You use the Traces folder in the STEP 7 project tree to create and manage traces.

Note:

The trace measurement data is available only within the STEP 7 project and is not available for processing by other tools.

The following figure shows the various steps of the trace feature:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/eoRTt58e_mmQ0wLRefVACw-VBkTPlmjVZAl17lebjV9hA/content?v=3c5893f57313c3e5)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/eoRTt58e_mmQ0wLRefVACw-VBkTPlmjVZAl17lebjV9hA)

|  |  |
| --- | --- |
| ① | Configure the trace in the trace editor of STEP 7. You can configure the following options:   - Data values to record - Recording duration - Recording frequency - Trigger condition |
| ② | Transfer the trace configuration from STEP 7 to the PLC. |
| ③ | The PLC executes the program, and when the trigger condition occurs, begins recording the trace data. |
| ④ | Transfer the recorded values from the PLC to STEP 7. |
| ⑤ | Use the tools in STEP 7 to analyze, graphically display, and save the data. |

The S7-1200 supports two trace jobs with a maximum of 16 variables captured per trigger event. Each trace job provides 524288 bytes of RAM for the recording of trace values and associated overhead, for example variable addresses and time stamps.

## Saving trace measurements to the memory card

The S7-1200 CPU can only save trace measurements to the SIMATIC memory card. If you do not have a memory card in your CPU, the CPU will log a diagnostics buffer entry if the program attempts to save trace measurements. The CPU limits the space allocated to trace measurements such that 1 MB of external load memory must always be available. If a trace measurement would require more memory than the maximum allowance, the CPU will not save the measurement and will log a diagnostics buffer entry.

In addition, if you select "Overwrite oldest recording" in STEP 7, the continual writing can reduce the lifetime of load memory. When you select "Overwrite oldest recording", the CPU replaces the oldest measurement with the newest measurement after it has stored the configured number of trace measurements, and continues tracing and saving measurements. Overwriting the oldest measurements is useful in capturing intermittent problems.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/~H5ypNH1IFHBJeGZXQWcYQ-VBkTPlmjVZAl17lebjV9hA/content?v=7b5df1b29c9f9f45)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/~H5ypNH1IFHBJeGZXQWcYQ-VBkTPlmjVZAl17lebjV9hA)

The CPU supports a maximum of 999 trace measurement results. During the time that the CPU is saving the trace measurements to external load memory, the CPU does not check the trigger condition for the trace job. Once the CPU finishes saving the trace measurements, the CPU resumes checking for trigger conditions.

## Access to examples

See the STEP 7 information system for details about how to program a trace, how to download the configuration, upload the trace data, and display the data in the logic analyzer. You can find detailed examples there in the "Using online and diagnostics functions > Using the trace and logic analyzer function" chapter.

In addition, the online manual ["Industry Automation SINAMICS/SIMATIC Using the trace and logic analyzer function"](https://support.industry.siemens.com/cs/ww/en/view/64897128) is an excellent reference.

---

## Determining the type of wire break condition from an SM 1231 module

As described in the topic [Measurement ranges of the analog inputs for current (SB and SM)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/7UfA8iIvArg5mBpr6B2bTQ?section=Xe9af61e2f1a658fa4ad822e017802a50), the SM 1231 module returns an analog input value of 32767 (16#7FFF) for both a wire break condition or an overflow condition. These conditions apply to the module only and not the channel. If you want to determine which of these two conditions occurred, you can include logic in your STEP 7 program to make the determination. The method to determine the condition type consists of these tasks:

- Create a Diagnostic error interrupt OB to be called whenever there is an incoming or outgoing diagnostic event.
- Include a call to the RALRM instruction.
- Set up an array of bytes for the AINFO parameter, which includes the information about the condition type.
- Evaluate bytes 32 and 33 of the AINFO structure of the RALRM\_DB when the CPU triggers the Diagnostic Interrupt OB..

## Creating a Diagnostic error interrupt OB

To be able to determine when a wire break condition occurs, create a Diagnostic error interrupt OB. The CPU will call this OB whenever an incoming or outgoing diagnostic event occurs.

When the CPU calls the Diagnostic error interrupt OB, the input parameter LADDR will contain the hardware identifier for the module with the error. You can find the hardware identifier for the SM 1231 module in the STEP 7 device configuration for the SM 1231 module.

## Calling the RALRM instruction

To program the RALRM instruction call, follow these steps:

1. Add a call to RALRM in your STEP 7 program.
2. Set the F\_ID input parameter to the hardware identifier in the LADDR parameter of the Diagnostic error interrupt OB.
3. Use an array of bytes for the TINFO and AINFO input parameters. Use an array size of 34 bytes or greater.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/5X~YiZYnxqEH4pHNjP_hsg-VBkTPlmjVZAl17lebjV9hA/content?v=d77ad724fec8de2a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/5X~YiZYnxqEH4pHNjP_hsg-VBkTPlmjVZAl17lebjV9hA)

## Interpreting AINFO after a diagnostic interrupt has occurred

The AINFO byte array will contain the information about the module diagnostics after the Diagnostic error interrupt OB executes.

Bytes 0 - 25 are header information. The bytes pertaining to the module diagnostic are as follows:

| **Byte** | **Description** | |
| --- | --- | --- |
| 26 and 27 | Word value 16#8000 - indicates the diagnostic is a PROFINET style diagnostic | |
| 28 and 29 | Word containing channel number responsible for this diagnostic | |
| 30 | Bit pattern aaabb000 that indicates the type of channel (aaa) and type of error (bb) | |
| aaa | bb |
| 000: reserved | 00: reserved |
| 001: input channel | 01: incoming error |
| 010: output channel | 10: outgoing error |
| 011: input/output channel | 11: outgoing error, other errors present |
| 31 | Indication of data format  0: Free data format  1: Bit  2: Two bits  3: Four bits  4: Byte  5: Word (two bytes)  6: Double word (four bytes)  7: Two double words (eight bytes) | |
| 32 and 33 | Word that defines the type of error:  16#0000: reserved  16#0001: short circuit  16#0002: undervoltage  16#0003: overvoltage  16#0004: overload  16#0005: over temperature  16#0006: wire break  16#0007: high limit exceeded  16#0008: low limit exceeded  16#0009: error | |

For example, consider bytes 26 - 33 of this AINFO structure:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/2AKzkjQ_Pl2H~qm_XJi8jw-VBkTPlmjVZAl17lebjV9hA/content?v=dba609d4f7dda55c)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/2AKzkjQ_Pl2H~qm_XJi8jw-VBkTPlmjVZAl17lebjV9hA)

- The Word at bytes 26 and 27 is 16#8000, which indicates that this is a Profinet style diagnostic.
- The Word at bytes 28 and 29 indicates this is a diagnostic for channel 0 or the module.
- Byte 30 is 16#28, which when interpreted as the bit pattern aaa bb 00 is 001 01 000. This value indicates that this diagnostic is for an input channel and is an incoming error.
- Byte 31 is 5, which indicates a Word value
- The word value at bytes 32 and 33 is 16#0007, which indicates high limit exceeded.

By capturing the AINFO information from a Diagnostic error interrupt event, you can thus determine the nature of the diagnostic event.

---

## Backing up and restoring a CPU


---

### Backup and restore options

You will make a number of changes to your automation system over time, for example, add new devices, replace existing devices or adapt the user program. If these changes were to result in undesirable behavior, you can restore the automation plant to an earlier version if you have a backup. STEP 7 and the S7‑1200 CPU offer different options for backing up and restoring the hardware configuration and software.

## Backup options

The table below provides an overview of the backup and restoration options of S7 CPUs:

|  | **Snapshot of the monitored values** | **Upload from device (software)** | **Upload device as new station (hardware and software)** | **Download backup from online device** |
| --- | --- | --- | --- | --- |
| **Use case** | Restoring a specific status of a data block.  The actual values of data blocks including time stamp are accepted in the project. | Upload blocks from a CPU to the project. | Upload of hardware configuration and software from a device to the project. | Create a complete backup of a CPU as a restore point. The backup copy is consistent and cannot be changed or opened. |
| **Requirement** | The CPU exists in a project. The data blocks must be identical online and offline. | The CPU exists in the project. | The device is available in the hardware catalog of TIA Portal. Any necessary HSPs or GSD files are installed. | - |
| **Possible in mode** | RUN, STOP | RUN, STOP | RUN, STOP | STOP |
| **Possible for F-CPUs** | Yes | Yes | No | Yes |
| **Backup can be edited** | Yes | Yes | Yes | No |

## Backup contents

The table below shows which data you can download and back up with which options:

|  | **Snapshot of the monitored values** | **Upload from device (software)** | **Upload device as new station (hardware and software)** | **Download backup from online device** |
| --- | --- | --- | --- | --- |
| **Actual values of the data blocks** | Snapshot is possible | Download is possible | Download is possible | Backup is possible |
| **Software blocks** | - | Download is possible | Download is possible | Backup is possible |
| **PLC tags (names of tags and constants)** | - | Download is possible | Download is possible | Backup is possible |
| **Technology objects** | - | Download is possible | Download is possible | Backup is possible |
| **Hardware configuration** | - | - | Download is possible | Backup is possible |
| **Monitoring tables (Web server)** | - | - | Download is not possible | Backup is possible |
| **Local data, bit memories, timers, counters and process picture** | Snapshot is not possible | Download is not possible | Download is not possible | Backup is possible |
| **Archives and recipes (PLC)** | - | - | - | Backup is possible |
| **General data on the SIMATIC memory card, for example, help for program blocks or GSD files** | - | - | - | Backup is possible |

## Special considerations during backup of actual values

The "Backup from online device" type of backup backs up the actual values of the tags that are set as retentive. To ensure consistency of the retentive data, disable all write access to retentive data during the backup.

A transition from STOP to RUN mode sets actual values of the non-retentive data to their start values. A CPU backup contains only the start values of non-retentive data.

---

### Backing up an online CPU

Making a backup of your configuration can be useful if you want to return to a specific configuration. You can restore the current configuration at a later time.

## Prerequisites

You can create as many backups as you want and store a variety of configurations for a CPU. To make a backup, you must meet the following prerequisites:

- You have already created the CPU in the STEP 7 project.
- You have connected the CPU to the programming device/PC directly using the PROFINET interface of the CPU. Backup and restore operations do not support the PROFIBUS interfaces of the CMs.
- The CPU is online. (If there is no online connection, the backup process establishes an online connection.)
- The CPU is in "STOP" mode. (If the CPU is not in STOP mode, the backup process prompts you to allow the CPU to go to STOP mode.)

## Procedure

To create a backup of the current configuration of a CPU, follow these steps:

1. Select the CPU in the project tree.
2. Select the "Backup from online device" command in the "Online" menu.

   If necessary, you must enter the password for read access to the CPU and confirm that the CPU should enter "STOP" mode.

## Result

The backups are named with the name of the CPU and the time and date of the backup. The backup includes all data that are needed to restore a particular configuration of a CPU. The CPU backs up the following data:

- Contents of the memory card if one is present and contents of internal load memory otherwise
- Retentive memory areas of data blocks, counters, and bit memory
- Other retentive memory contents, such as IP address parameters

The backup contains the current values of the CPU but does not include the diagnostics buffer.

The backup does not contain the password for protection of confidential PLC configuration data.

You can find the backup in the project tree under the CPU in the "Online backups" folder. The following figure shows an S7-1200 CPU for which two backups have been created:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/eJKVPd01FhOMGUbBzQT67Q-VBkTPlmjVZAl17lebjV9hA/content?v=34cea5144767bca9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/eJKVPd01FhOMGUbBzQT67Q-VBkTPlmjVZAl17lebjV9hA)

Note:

Note that you can also back up the online CPU from the SIMATIC Automation Tool (SAT) or the [Web server Online backup standard Web page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/isBliVNTXNJ6NCzfBBr7pg?section=X10d08635decfd77ea365a39fc4668fd0).

When you back files up from STEP 7, STEP 7 stores the files within the STEP 7 project. When you back files up from the Web server, your PC or device saves the backup files in the default folder for downloads. You cannot restore STEP 7 backup files from the Web server and you cannot restore Web server backup files from STEP 7. You can, however, save STEP 7 backup files directly to the download folder of your PC or device. If you do so, then you can restore these files from the Web server.

## Saving backup files to your PC or device

To save a backup file to your PC or device, follow these steps:

1. Right-click a file from the Online backups folder in the project tree.
2. Select "Save as" from the context menu.
3. Navigate to the folder where you want to save the file, for example the default folder for downloads on your PC or device.
4. Click Save.

---

### Restoring a CPU

If you have backed up the configuration of a CPU at an earlier point in time, you can transfer the backup to the CPU. The CPU goes to STOP while restoring a backup. If an access level is configured for the CPU, you must supply the password for read access to the CPU.

The backup does not contain the password for protection of confidential PLC configuration data.

Warning:

**Potential cybersecurity risks during Restore**

If the Restore process is interrupted and you power cycle the CPU before the Restore process is complete, this causes the CPU to lose previously configured protection levels. This can allow attackers with network access to potentially disrupt process operation.

Set up your CPU in a secure environment. When a Restore operation is in progress, do not power cycle the CPU. If a power outage occurs during a Restore operation, retry the operation after power has been restored.

Disruption of process operation can result in death, severe personal injury, and/or property damage.

Warning:

**Restoring backups with unknown content**

If you restore a backup with unknown content, you can cause malfunctions or program errors.

Make sure that the backup consists of a configuration with known content.

Malfunction and/or program errors can result in death, severe personal injury, and/or property damage.

## Restoring a backup to a CPU that has protection of confidential PLC configuration data

If your CPU has [protection of confidential PLC configuration data](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/weZr~222uiVd9iOtUdI3Ug?section=X28ad57bb3d4f1e3452505460378b64b3), make sure that the configured password in the backup file for protection of confidential PLC configuration data matches the one in the CPU.

If the passwords do not match, the CPU cannot go to RUN mode.

if you attempt to restore a backup file that has a different password for the protection of confidential PLC configuration data than the CPU, the restore succeeds. The CPU, however, will restart in an error state because the protection of confidential PLC configuration data in the CPU did not match the one in the project you restored to the CPU.

In this case, you must set the protection of confidential PLC configuration data in the CPU to match the project that you restored. You can use one of these ways to set or delete the password for protection of confidential PLC configuration data that is in the CPU:

- SIMATIC Automation Tool V4.0 SP3 or greater
- TIA Portal, [Online & Diagnostics](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/TanNmrtmqi3RdpZATLIxkg?section=X428ad9a0212de5508369e0d124d4f606)
- [SIMATIC memory card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vigU7rJrF3NUV8Dx9ahVDg?section=Xac2688e7353037b616906099600e725d)

## Prerequisites

To restore a backup, you must meet the following prerequisites:

- The STEP 7 project includes a configuration for the CPU and a previously-made backup.
- The CPU is connected to the programming device directly through the PROFINET interface of the CPU.
- The CPU is in STOP mode.
- You know the password for full access to the CPU, if an [access level](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/boJrawCTV7~GzOYPMsNOtA?section=X6b7b6de0ce1887813501b51c2fcc624a) was configured.

## Procedure

To restore a backup, follow these steps:

1. Open the CPU in the project tree to display the lower-level objects.
2. Select the backup you want to restore from the "Online backups" folder.
3. From the "Online" menu, select the "Download to device" command.

   - If you had previously [established an online connection](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/DD0kYV~aBXliwFCstTwS8Q?section=X697e6c023185521f532da290cbe45678), the "Load preview" dialog opens. This dialog displays alarms and recommends actions needed for the loading operation.
   - If you had not previously established an online connection, the "Extended download to device" dialog opens, and you must first select the interface from which you want to establish the online connection to the CPU.
4. Check the alarms in the "Load preview" dialog, and select the actions in the "Action" column, if necessary.
5. Click the "Load" button (The "Load" button is selectable as soon as downloading is possible.)
6. STEP 7 restores the backup to the CPU. From the "Load results" dialog, you can check whether or not the loading operation was successful and take any further action that might be necessary.
7. After reviewing the "Load results" dialog, click the "Finish" button.

   If prompted, enter the password for full access to the CPU and confirm that the CPU can enter "STOP" mode.

   STEP 7 restores the contents of the backup to the CPU and restarts the CPU.

Note:

Note that you can also restore a CPU backup from the [Web server Online backup standard Web page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/isBliVNTXNJ6NCzfBBr7pg?section=X10d08635decfd77ea365a39fc4668fd0).