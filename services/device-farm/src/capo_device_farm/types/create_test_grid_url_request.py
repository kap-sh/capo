"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateTestGridUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_farm_arn
    import capo_device_farm.types.test_grid_url_expires_in_seconds_input


class CreateTestGridUrlRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>ARN (from <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>) to associate with the short-term URL. </p>"""
    expires_in_seconds: "capo_device_farm.types.test_grid_url_expires_in_seconds_input.TestGridUrlExpiresInSecondsInput"
    """<p>Lifetime, in seconds, of the URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTestGridUrlRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["expiresInSeconds"] = value["expires_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTestGridUrlRequest:
    out: CreateTestGridUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
    if data.get("expiresInSeconds") is not None:
        out["expires_in_seconds"] = data["expiresInSeconds"]
    else:
        out["expires_in_seconds"] = 0
    return out
