"""Generated from Smithy shape ``com.amazonaws.billing#DecimalAmountString``."""

from typing import TypeAlias

"""<p>The amount, as a decimal string with at most six decimal places, for example <code>2400.000000</code>. The amount is always in the currency of the credit, so unlike <code>Amount</code> it carries no currency code. A decimal string, not a floating-point number, lets portions add up exactly to a balance.</p>"""
DecimalAmountString: TypeAlias = str
