# Device exchange and spare parts compatibility


---

## Replacing a CPU that has protection of confidential configuration data

The assignment of passwords to protect confidential PLC configuration data also has an impact on the replacement parts scenario.

## Rules for the replacement parts scenario

Observe the following rules for the replacement parts scenario:

**Configuration of the replacement CPU via TIA Portal**

- If possible, use a CPU that does not have a project configuration or a configured password for protection of confidential PLC configuration data as the replacement CPU.

  Advantage: You can load the project into the replacement CPU without any further preparation.
- If the replacement CPU has already been configured, you must [reset the CPU to the factory settings](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ousE3DGfufW3uTupUTcVWA?section=X491b26087c13e566b0ce80df762d767a) and select these options:

  - Delete password for protection of confidential PLC configuration data
  - Format memory card, if the CPU has a memory card

## Replacing a CPU with configuration data on a SIMATIC memory card

- If you have **not** assigned a password to a CPU in your project to protect confidential PLC configuration data, you can insert the memory card of the CPU to be replaced into a new, unused CPU without any further action.
- If the replacement CPU has already been configured with a password, you must first [reset this CPU to the factory settings](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ousE3DGfufW3uTupUTcVWA?section=X491b26087c13e566b0ce80df762d767a) using the option "Delete password for protection of confidential PLC configuration data".
- If you have assigned the same password for protection of confidential PLC configuration data to a group of CPUs, you can also assign the group password to the replacement CPU from the [device configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/weZr~222uiVd9iOtUdI3Ug?section=X28ad57bb3d4f1e3452505460378b64b3) in the TIA Portal. In this case you can, for example, insert a memory card with the current project into the CPU and put it into operation without any further password handling.
- If you assign different passwords to each CPU in your project, [go online](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/DD0kYV~aBXliwFCstTwS8Q?section=X697e6c023185521f532da290cbe45678) and set the password for protection of confidential data for the replacement CPU with the online and diagnostics tools. [Select "Set password to protect confidential PLC configuration data" from the online functions.](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/TanNmrtmqi3RdpZATLIxkg?section=X428ad9a0212de5508369e0d124d4f606)

---

## Exchanging a V3.0 CPU for a V4.x CPU

To upgrade a V3.0 CPU to a V4.x CPU, you must replace the CPU hardware. You cannot upgrade a V3.0 CPU to a V4.x CPU by firmware update.

Then in your STEP 7 project, you can [replace your V3.0 CPU with a V4.x CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_Uks9OtckTK2vxyOElULHQ?section=X74702a1c9b29d6e5f29443d9a98c2b7d) and use your existing STEP 7 project that you designed for the V3.0 CPU.

When you replace a V3.0 CPU with a V4.x CPU, you might also want to check for and apply [firmware updates](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/2_4~8k2RDOs~~ji0BO4dRQ?section=Xe2bb67aff193f4fb2925b9ca97391dce) to your connected signal and communication modules.

Note:

**No device exchange possible in STEP 7 from V4.x to V3.0**

You can exchange a V3.0 CPU for a V4.x CPU, but you cannot exchange a V4.x CPU for a V3.0 CPU after you download the configuration. If you want to view or otherwise use your existing STEP 7 project for a V3.0 CPU, make an archive of your project prior to the device exchange.

Note that if you have not downloaded the exchanged device configuration, you can undo it. After downloading, however, you cannot undo the device exchange from V3.0 to V4.x.

You need to be aware of some configuration and operational changes between the two CPU versions.

## Upgrading STEP 7 projects

To work with a STEP 7 project that is STEP 7 V13 or older, you must first upgrade the project to STEP 7 V13 SP1 or SP2. Then you can upgrade the STEP 7 V13 SPx project to the current STEP 7 version.

Warning:

**Risks with editing and executing program logic from older versions of STEP 7**

You cannot upgrade a project that is STEP 7 V13 or older to the current version by copying program logic.

You must upgrade your STEP 7 project as defined above.

Executing STEP 7 program logic that you copied from an older version to a newer version can cause unpredictable program behavior and can result in death or severe personal injury.

## Organization blocks

You can configure OB execution to be [interruptible or non-interruptible](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ZzTkqIXOXL5KUP6Zmf0K7Q?section=Xc906da4a10094d33e122df8df9998981). In projects from V3.0 CPUs, STEP 7 set all OBs by default to be non-interruptible.

STEP 7 sets all [OB priorities](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ZzTkqIXOXL5KUP6Zmf0K7Q?section=Xc906da4a10094d33e122df8df9998981) to the values they were in the V3.0 CPU STEP 7 project.

You can subsequently change the interruption or priority settings if you choose.

The [Diagnostic error interrupt OB](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/R5Bw4gpcYCa_T2vrPmSNdg?section=X5bd1ad371679d68bf380b14e776a256b) start information references the submodule as a whole if no diagnostics event is pending.

## CPU password protection

STEP 7 sets the [password protection level](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/boJrawCTV7~GzOYPMsNOtA?section=X6b7b6de0ce1887813501b51c2fcc624a) for the V4.x CPU to be the equivalent password protection level that was set for the V3.0 CPU, and assigns the V3.0 password to the "Full access (no protection)" password for the V4.x CPU:

| V3.0 protection level | V4.x access level |
| --- | --- |
| No protection | Full access (no protection) |
| Write protection | Read access |
| Write/read protection | HMI access |

Note that the V4.x access level "No access (complete protection)" did not exist for V3.0.

## Web server

If you use user-defined Web pages in your V3.0 project, store them in your project installation folder under the subfolder "UserFiles\Webserver" prior to upgrading your project. If you store your user-defined pages at this location, saving the STEP 7 project will also save the user-defined Web pages.

If you exchange a V3.0 CPU for a V4.x CPU, your [Web server project setting](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zhgg0gJgOhxaX6BVSPQiIA?section=Xd1f721b46269feb9a0bd64cba8b230f3) for activating the Web server and HTTPS setting will be the same as it was in V3.0. You can then configure [users, privileges, passwords](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/U6rqe7jrqQ4xhozuLIAzEg?section=Xfe7402828f2010de737c95f47cae4785), and [languages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Zhgg0gJgOhxaX6BVSPQiIA?section=Xd1f721b46269feb9a0bd64cba8b230f3) as needed to use the Web server. If you do not configure users with additional privileges, then you are limited as to what you can view from the [standard Web pages](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/wYbAoKDX_XQ_9F0P~5rJkg?section=X165292e35124f741a26d2259be560c6f). The S7‑1200 V4.x CPU does not support the former pre-configured "admin" user and password.

The S7-1200 V3.0 Web server Data log page provided a "Download and Clear" operation. The V4.x Web server [File browser page](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/f1bXzgmsxyQgQcYAqC77rA?section=X81170b06653aefc28fb2399202cdb341), from which you access data logs, no longer provides this feature. Instead, the Web server provides the ability to download and delete data log files.

## Transfer card incompatibility

You cannot use a V3.0 [transfer card](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/~1RciNXiXr74E8iWWII9UQ?section=X5c27266998836f300f5c5d72e823d99a) to transfer a V3.0 program to a V4.x CPU. You must open the V3.0 project in STEP 7, [change the device to a V4.x CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_Uks9OtckTK2vxyOElULHQ?section=X74702a1c9b29d6e5f29443d9a98c2b7d), and download the STEP 7 project to your V4.x CPU. After you have changed your project to a V4.x project, you can then make a V4.x transfer card for subsequent program transfers.

## GET/PUT communication

By default, S7‑1200 V3.0 CPUs enabled GET/PUT communication. When you [replace your V3.0 CPU with a V4.x CPU](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/_Uks9OtckTK2vxyOElULHQ?section=X74702a1c9b29d6e5f29443d9a98c2b7d), you see a message in the compatibility information section stating that GET/PUT is enabled.

## Motion control support

S7‑1200 V4.x CPUs do not support the V1.0 and V2.0 motion libraries. If you perform a device exchange for a STEP 7 project with V1.0 or V2.0 motion libraries, the device exchange substitutes compatible V3.0 [motion control instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/yAOoJX3~riuvK7YWWuBSVw?section=X2394810341afd9788c4c16972f8c0baf) for the V1.0 or V2.0 motion library instructions at compile.

If you perform a device exchange from a V3.0 CPU to a V4.x CPU for a STEP 7 project that contains two different motion control instruction versions (V3.0 and V5.0), the device exchange substitutes compatible V5.0 [motion control instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/yAOoJX3~riuvK7YWWuBSVw?section=X2394810341afd9788c4c16972f8c0baf) at compile.

During a device exchange from a V3.0 CPU to a V4.x CPU, the motion control Technological Object (TO) version does not automatically change from V3.0 to V5.0. If you want to upgrade to the later versions, you must go to the Instruction tree and select the required S7‑1200 Motion Control version for your project.

The S7-1200 V4.x CPU allows the following motion control versions:

- V3.0
- V4.0
- V5.0
- V6.0

The TO structure is different between motion control versions V3.0 and V5.0. All associated blocks change as well. Block interfaces, watch tables, and traces update to the new motion control V5.0 structure. You can find the differences between the V3.0 CPU and V4.x CPU motion control axis parameters in the following two tables:

| V3.0 CPU  (Motion control V3.0)​ | V4.x CPU  (Motion control V5.0) |
| --- | --- |
| Config.General.LengthUnit | Units.LengthUnit |
| Config.Mechanics.PulsesPerDriveRevolution | Actor.DriveParameter.PulsesPerDriveRevolution |
| Config.Mechanics.LeadScrew | Mechanics.LeadScrew |
| Config.Mechanics.InverseDirection | Actor.InverseDirection |
| Config.DynamicLimits.MinVelocity | DynamicLimits.MinVelocity |
| Config.DynamicLimits.MaxVelocity | DynamicLimits.MaxVelocity |
| Config.DynamicDefaults.Acceleration | DynamicDefaults.Acceleration |
| Config.DynamicDefaults.Deceleration | DynamicDefaults.Deceleration |
| Config.DynamicDefaults.EmergencyDeceleration | DynamicDefaults.EmergencyDeceleration |
| Config.DynamicDefaults.Jerk | DynamicDefaults.Jerk |
| Config.PositionLimits\_SW.Active | PositionLimitsSW.Active |
| Config.PositionLimits\_SW.MinPosition | PositionLimitsSW.MinPosition |
| Config.PositionLimits\_SW.MaxPosition | PositionLimitsSW.MaxPosition |
| Config.PositionLimits\_HW.Active | PositionLimitsHW.Active |
| Config.PositionLimits\_HW.MinSwitchedLevel | PositionLimitsHW.MinSwitchLevel |
| Config.PositionLimits\_HW.MaxSwitchedLevel | PositionLimitsHW.MaxSwitchLevel |
| Config.Homing.AutoReversal | Homing.AutoReversal |
| Config.Homing.Direction | Homing.ApproachDirection |
| Config.Homing.SideActiveHoming | Sensor[1].ActiveHoming.SideInput |
| Config.Homing.SidePassiveHoming | Sensor[1].PassiveHoming.SideInput |
| Config.Homing.Offset | Sensor[1].ActiveHoming.HomePositionOffset |
| Config.Homing.FastVelocity | Homing.ApproachVelocity |
| Config.Homing.SlowVelocity | Homing.ReferencingVelocity |
| MotionStatus.Position | Position |
| MotionStatus.Velocity | Velocity |
| MotionStatus.Distance | StatusPositioning.Distance |
| MotionStatus.TargetPosition | StatusPositioning.TargetPosition |
| StatusBits.SpeedCommand | StatusBits.VelocityCommand |
| StatusBits.Homing | StatusBits.HomingCommand |

The only "commandtable" parameter that is renamed is the array with the commands:

| V3.0 | V4.x |
| --- | --- |
| Config.Command[] | Command[] |

Note: The array "Command[]" is a UDT of the type "TO\_CmdTab\_Config\_Command" in V3.0 and "TO\_Struct\_Command" in V4.x.

## Instruction changes

The following instructions have changes in parameters or behavior:

- [RDREC and WRREC](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PiEg0pt~LlUmwS9L6Smg~Q?section=X43e7bcab851ce87a78cb1ffa9551bf8f)
- [CONV](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ybVmzRp9F~qhpNLCMzdDjQ?section=X2dadd20c60f8186a3c45081868d2d4e1)

## HMI panel communication

If you had one or more [HMI panels](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PtcC_3qLaq2FNgz5TEz18Q?section=X6d3ebec9f5f5c4d0b1bf22170aa3e636) connected to your S7-1200 V3.0 CPU, the communication to the S7-1200 V4.x CPU depends on the type of communication you use and the firmware version of the HMI panel. Recompile and download your project to the CPU and the HMI and/or update your HMI firmware.

## Requirement to recompile program blocks

After exchanging a V3.0 CPU for a V4.x CPU, you must recompile all program blocks before you can download them to the V4.x CPU. Additionally, if any of the blocks have [know-how protection](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/QHw~mfwuSzKV9AZLKNqsYw?section=Xc2e06ca3350b2e8e8e3c069896da8203) or [copy protection bound to a PLC serial number](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/uPySt3Pz5TRLltQsxMhX9g?section=Xa63b7a68c88ce8e0e33341135882c9bc), you must remove the protection before you compile and download the blocks. (You do not, however, need to deactivate copy protection bound to a memory card.) After a successful compile, you can reconfigure the know-how protection and/or PLC serial number copy protection. Note that if your project includes any blocks with know-how protection that an OEM (Original Equipment Manufacturer) provided, you must contact the OEM to provide V4.x versions of those blocks.

In general, Siemens recommends that you recompile the hardware configuration and software in STEP 7 and download to all devices in your project after the device exchange. Correct any errors that compiling the project finds, and recompile until you have no errors. Then, you can download the project to the V4.x CPU.

## S7‑1200 V3.0 projects might not fit in S7‑1200 V4.x CPUs

S7-1200 V4.0 and later added a reserve area of 100 bytes to each DB to support download without reinitialization.

You can remove the 100-byte reserve area from DBs prior to attempting to download a V3.0 project to a V4.x CPU.

To remove the 100-byte reserve area, follow these steps before you perform the device exchange:

1. From the TIA Portal main menu, select the Options > Settings menu command.
2. From the navigation tree, open the PLC programming > General node.
3. In the "Download without reinitialization" area, set the memory reserve to 0 bytes.

   [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/8zAJQN7niOsUrfMpwgUTtg-VBkTPlmjVZAl17lebjV9hA/content?v=870f4867fe9dcfe1)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8zAJQN7niOsUrfMpwgUTtg-VBkTPlmjVZAl17lebjV9hA)

If you have already performed the device exchange, you must remove the 100-byte reserve from each block individually:

1. From the project tree, right-click a data block from the Program blocks folder and select Properties from the shortcut menu.
2. In the Data block properties dialog, select the "Download without reinitialization" node.
3. Set the memory reserve to 0 bytes.
4. Repeat for each data block in your project.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/auJISv0DQ2flAR_V_NV2Ig-VBkTPlmjVZAl17lebjV9hA/content?v=d101218e75d582bf)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/auJISv0DQ2flAR_V_NV2Ig-VBkTPlmjVZAl17lebjV9hA)

---

## S7-1200 V3.0 and earlier terminal block spare kits

Table 1. S7-1200 CPU V3.0 and earlier - Terminal Block spare kits

| **If you have S7-1200 CPU V3.0 and earlier (article number)** | **Use this terminal block spare kit (4/pk)** | |
| --- | --- | --- |
| **Terminal block article number** | **Terminal block description** |
| CPU 1211C DC/DC/DC (6ES7211-1AE31-0XB0) | 6ES7292-1BC30-0XA0  6ES7292-1AH30-0XA0  6ES7292-1AP30-0XA0 | 3 pin, gold-plated  8 pin, gold-plated  14 pin, tin-plated |
| CPU 1211C AC/DC/Relay (6ES7211-1BE31-0XB0) |
| CPU 1211C DC/DC/Relay (6ES7211-1HE31-0XB0) |
| CPU 1212C DC/DC/DC (6ES7212-1AE31-0XB0) |
| CPU 1212C AC/DC/Relay (6ES7212-1BE31-0XB0) |
| CPU 1212C DC/DC/Relay (6ES7212-1HE31-0XB0) |
| CPU 1214C DC/DC/DC (6ES7214-1AG31-0XB0) | 6ES7292-1BC30-0XA0  6ES7292-1AM30-0XA0  6ES7292-1AV30-0XA0 | 3 pin, gold-plated  12 pin, tin-plated  20 pin, tin-plated |
| CPU 1214C AC/DC/Relay (6ES7214-1BG31-0XB0) |
| CPU 1214C DC/DC/Relay (6ES7214-1HG31-0XB0) |
| CPU 1215C DC/DC/DC (6ES7215-1AG31-0XB0) | 6ES7292-1BF30-0XB0  6ES7292-1AM30-0XA0  6ES7292-1AV30-0XA0 | 6 pin, gold-plated  12 pin, tin-plated  20 pin, tin-plated |
| CPU 1215C AC/DC/Relay (6ES7215-1BG31-0XB0) |
| CPU 1215C DC/DC/Relay (6ES7215-1HG31-0XB0) |

Table 2. S7-1200 SMs V3.0 and earlier - Terminal Block spare kits

| **If you have S7-1200 SM V3.0 and earlier (article number)** | **Use this terminal block spare kit (4/pk)** | |
| --- | --- | --- |
| **Terminal block article number** | **Terminal block description** |
| SM 1221 DI 8 x DC (6ES7221-1BF30-0XB0) | 6ES7292-1AG30-0XA0 | 7 pin, tin-plated |
| SM 1222 DQ 8 x DC (6ES7222-1BF30-0XB0) |
| SM 1222 DQ 8 x Relay (6ES7222-1HF30-0XB0) |
| SM 1231 AI 4 x 13 bit (6ES7231-4HD30-0XB0) | 6ES7292-1BG30-0XA0 | 7 pin, gold-plated |
| SM 1232 AQ 2 x 14 bit (6ES7232-4HB30-0XB0) |
| SM 1231 AI 4 x TC (6ES7231-5QD30-0XB0) |
| SM 1231 AI 4 x 16 bit (6ES7231-5ND30-0XB0) |
| SM 1221 DI 16 x DC (6ES7221-1BH30-0XB0) | 6ES7292-1AG30-0XA0 | 7 pin, tin-plated |
| SM 1222 DQ 16 x DC (6ES7222-1BH30-0XB0) |
| SM 1222 DQ 16 x Relay (6ES7222-1HH30-0XB0) |
| SM 1223 DI 8 x DC/DQ 8x DC (6ES7223-1BH30-0XB0) |
| SM 1223 8 x DC/8 x Relay (6ES7223-1PH30-0XB0) |
| SM 1223 8 x AC/8 x Relay (6ES7223-1QH30-0XB0) |
| SM 1234 AI 4 / AQ 2 (6ES7234-4HE30-0XB0) | 6ES7292-1BG30-0XA0 | 7 pin, gold-plated |
| SM 1231 AI 8 x 13 bit (6ES7231-4HF30-0XB0) |
| SM 1232 AQ 4 x 14 bit (6ES7232-4HD30-0XB0) |
| SM 1231 AI 4 x RTD (6ES7231-5PD30-0XB0) |
| SM 1231 AI 8 x TC (6ES7231-5QF30-0XB0) |
| SM 1222 DQ 8 x Relay (Changeover) (6ES7222‑1XF30‑0XB0) | 6ES7292-1AL30-0XA0 | 11 pin, tin-plated |
| SM 1223 DI 16 x DC/DQ 16 x DC (6ES7223-1BL30-0XB0) |
| SM 1223 16 x DC/16 x Relay (6ES7223-1PL30-0XB0) |
| SM 1231 AI 8 x RTD (6ES7231-5PF30-0XB0) | 6ES7292-1BL30-0XA0 | 11 pin, gold-plated |