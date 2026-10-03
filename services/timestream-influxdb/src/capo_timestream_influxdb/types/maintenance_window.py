"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#MaintenanceWindow``."""

from typing import TypeAlias

"""Preferred maintenance window in format "ddd:HH:MM-ddd:HH:MM" Format requirements: - Day: Mon, Tue, Wed, Thu, Fri, Sat, Sun - Hour: 00-23 (24-hour format, 2 digits) - Minute: 00-59 (2 digits) Provide empty string to let the system choose a window. Examples: - "Sun:02:00-Sun:06:00" (4-hour window Sunday morning) - "Sat:23:00-Sun:03:00" (cross-midnight window) - "" or (system chooses)"""
MaintenanceWindow: TypeAlias = str
