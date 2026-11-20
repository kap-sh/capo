"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#S3Uri``."""

from typing import TypeAlias

"""An `s3://` URI naming a partner-supplied file. <p>Appears only as a request input. The service never echoes a raw S3 URI back to a caller — a read returns a URL, or for a PII file no location at all."""
S3Uri: TypeAlias = str
