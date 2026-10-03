"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Permit2AllowanceLimit``."""

from typing import TypeAlias

"""<p>The maximum on-chain Permit2 allowance to grant, in the asset's smallest denomination. Pass the value as a numeric string. For example, "1000000" is 1 USDC at 6 decimals. To grant an unlimited allowance, pass the uint256 maximum, which is a 78-digit number.</p>"""
Permit2AllowanceLimit: TypeAlias = str
