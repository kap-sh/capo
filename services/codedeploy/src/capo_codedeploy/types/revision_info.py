"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.generic_revision_info
    import capo_codedeploy.types.revision_location


class RevisionInfo(TypedDict, closed=True):
    revision_location: NotRequired[
        "capo_codedeploy.types.revision_location.RevisionLocation"
    ]
    """<p>Information about the location and type of an application revision.</p>"""
    generic_revision_info: NotRequired[
        "capo_codedeploy.types.generic_revision_info.GenericRevisionInfo"
    ]
    """<p>Information about an application revision, including usage details and associated deployment groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionInfo) -> dict:
    out: dict = {}
    if "revision_location" in value:
        import capo_codedeploy.types.revision_location

        out["revisionLocation"] = (
            capo_codedeploy.types.revision_location.serialize_aws_json_1_1(
                value["revision_location"]
            )
        )
    if "generic_revision_info" in value:
        import capo_codedeploy.types.generic_revision_info

        out["genericRevisionInfo"] = (
            capo_codedeploy.types.generic_revision_info.serialize_aws_json_1_1(
                value["generic_revision_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevisionInfo:
    out: RevisionInfo = {}  # type: ignore[typeddict-item]
    if data.get("revisionLocation") is not None:
        import capo_codedeploy.types.revision_location

        out["revision_location"] = (
            capo_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revisionLocation"]
            )
        )
    if data.get("genericRevisionInfo") is not None:
        import capo_codedeploy.types.generic_revision_info

        out["generic_revision_info"] = (
            capo_codedeploy.types.generic_revision_info.deserialize_aws_json_1_1(
                data["genericRevisionInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevisionInfo) -> dict:
    out: dict = {}
    if "revision_location" in value:
        import capo_codedeploy.types.revision_location

        out["revisionLocation"] = (
            capo_codedeploy.types.revision_location.serialize_cbor(
                value["revision_location"]
            )
        )
    if "generic_revision_info" in value:
        import capo_codedeploy.types.generic_revision_info

        out["genericRevisionInfo"] = (
            capo_codedeploy.types.generic_revision_info.serialize_cbor(
                value["generic_revision_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RevisionInfo:
    out: RevisionInfo = {}  # type: ignore[typeddict-item]
    if data.get("revisionLocation") is not None:
        import capo_codedeploy.types.revision_location

        out["revision_location"] = (
            capo_codedeploy.types.revision_location.deserialize_cbor(
                data["revisionLocation"]
            )
        )
    if data.get("genericRevisionInfo") is not None:
        import capo_codedeploy.types.generic_revision_info

        out["generic_revision_info"] = (
            capo_codedeploy.types.generic_revision_info.deserialize_cbor(
                data["genericRevisionInfo"]
            )
        )
    return out
