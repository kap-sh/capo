"""Generated from Smithy shape ``com.amazonaws.drs#StrictDRSARN``."""

from typing import TypeAlias

"""Strict ARN type for Recovery Plan resources. Only allows safe characters in the resource portion — rejects HTML/script injection characters (<, >, ", ', etc.) per AWS API input validation standards. Resource portion allows: [A-Za-z0-9_/.-] which covers all DRS recovery plan resource identifiers (plan-xxx, st-xxx, exec-xxx, step-xxx)."""
StrictDRSARN: TypeAlias = str
