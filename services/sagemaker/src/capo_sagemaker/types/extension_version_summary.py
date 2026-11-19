"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_version


class ExtensionVersionSummary(TypedDict, closed=True):
    extension_version: NotRequired[
        "capo_sagemaker.types.extension_version.ExtensionVersion"
    ]
    """<p>The version of the extension, in <code>MAJOR.MINOR.PATCH</code> format, for example <code>1.0.0</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionVersionSummary) -> dict:
    out: dict = {}
    if "extension_version" in value:
        out["ExtensionVersion"] = value["extension_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtensionVersionSummary:
    out: ExtensionVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionVersion") is not None:
        out["extension_version"] = data["ExtensionVersion"]
    return out
