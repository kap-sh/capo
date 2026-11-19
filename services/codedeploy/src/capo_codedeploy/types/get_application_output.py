"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetApplicationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_info


class GetApplicationOutput(TypedDict, closed=True):
    application: NotRequired["capo_codedeploy.types.application_info.ApplicationInfo"]
    """<p>Information about the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationOutput) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_codedeploy.types.application_info

        out["application"] = (
            capo_codedeploy.types.application_info.serialize_aws_json_1_1(
                value["application"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationOutput:
    out: GetApplicationOutput = {}  # type: ignore[typeddict-item]
    if data.get("application") is not None:
        import capo_codedeploy.types.application_info

        out["application"] = (
            capo_codedeploy.types.application_info.deserialize_aws_json_1_1(
                data["application"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetApplicationOutput) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_codedeploy.types.application_info

        out["application"] = capo_codedeploy.types.application_info.serialize_cbor(
            value["application"]
        )
    return out


def deserialize_cbor(data: dict) -> GetApplicationOutput:
    out: GetApplicationOutput = {}  # type: ignore[typeddict-item]
    if data.get("application") is not None:
        import capo_codedeploy.types.application_info

        out["application"] = capo_codedeploy.types.application_info.deserialize_cbor(
            data["application"]
        )
    return out
