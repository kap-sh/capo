"""Generated from Smithy shape ``com.amazonaws.endusermessaging#MediaDownloadUrl``."""

from typing import TypeAlias

"""Presigned S3 GET URL for downloading attribute media. Marked `@sensitive` because the URL carries a SigV4 signature that grants object-read for the expiry window (1 hour). Without this trait the value would land in generated SDK `Debug` output and from there into log retention."""
MediaDownloadUrl: TypeAlias = str
