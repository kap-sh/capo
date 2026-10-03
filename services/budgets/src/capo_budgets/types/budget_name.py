"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetName``."""

from typing import TypeAlias

r"""<p> A string that represents the budget name. The ":" and "\" characters, and the "/action/" substring, aren't allowed.</p> <p>Budget names are validated for content. Names that contain phone numbers, URLs, or email addresses combined with certain terms may be rejected.</p>"""
BudgetName: TypeAlias = str
