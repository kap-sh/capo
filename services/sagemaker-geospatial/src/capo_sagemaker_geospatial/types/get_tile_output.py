"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTileOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.binary_file


class GetTileOutput(TypedDict, closed=True):
    binary_file: "capo_sagemaker_geospatial.types.binary_file.BinaryFile"
    """<p>The output binary file.</p>"""


def redact_sensitive(value: GetTileOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "binary_file" in value:
        out["binary_file"] = "*** Streaming Data Redacted ***"
    return out
