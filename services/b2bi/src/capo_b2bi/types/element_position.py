"""Generated from Smithy shape ``com.amazonaws.b2bi#ElementPosition``."""

from typing import TypeAlias

"""<p>A string type representing the position of an element within an X12 segment. The format follows the pattern of segment identifier followed by element position (e.g., "ST-01" for the first element of the ST segment) and optionally a component position (e.g., "ST-01-02" for the second component of the first element). This type is used in validation rules to precisely identify which element in which position is being validated.</p>"""
ElementPosition: TypeAlias = str
