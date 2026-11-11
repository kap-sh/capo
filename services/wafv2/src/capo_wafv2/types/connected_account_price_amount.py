"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountPriceAmount``."""

from typing import TypeAlias

"""<p>The price per request for a connected account, as a decimal string. Valid values range from 0.01 to 999999.99 USDC, with up to two decimal places. Sub-cent amounts are not supported.</p>"""
ConnectedAccountPriceAmount: TypeAlias = str
