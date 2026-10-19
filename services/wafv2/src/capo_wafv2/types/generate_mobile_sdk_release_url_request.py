"""Generated from Smithy shape ``com.amazonaws.wafv2#GenerateMobileSdkReleaseUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.platform
    import capo_wafv2.types.version_key_string


class GenerateMobileSdkReleaseUrlRequest(TypedDict, closed=True):
    platform: "capo_wafv2.types.platform.Platform"
    """<p>The device platform.</p>"""
    release_version: "capo_wafv2.types.version_key_string.VersionKeyString"
    """<p>The release version. For the latest available version, specify <code>LATEST</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateMobileSdkReleaseUrlRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.platform

    out["Platform"] = capo_wafv2.types.platform.serialize_aws_json_1_1(
        value["platform"]
    )
    out["ReleaseVersion"] = value["release_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateMobileSdkReleaseUrlRequest:
    out: GenerateMobileSdkReleaseUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("Platform") is not None:
        import capo_wafv2.types.platform

        out["platform"] = capo_wafv2.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    else:
        import typing

        out["platform"] = typing.cast("capo_wafv2.types.platform.Platform", "")
    if data.get("ReleaseVersion") is not None:
        out["release_version"] = data["ReleaseVersion"]
    else:
        out["release_version"] = ""
    return out
