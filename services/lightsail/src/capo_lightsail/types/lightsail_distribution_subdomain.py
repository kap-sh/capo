"""Generated from Smithy shape ``com.amazonaws.lightsail#LightsailDistributionSubdomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.lightsail_distribution_subdomain_state_enum
    import capo_lightsail.types.string


class LightsailDistributionSubdomain(TypedDict, closed=True):
    name: "capo_lightsail.types.string.string"
    """<p>The subdomain (for example, <code>mysite</code>), not its web address.</p>"""
    state: "capo_lightsail.types.lightsail_distribution_subdomain_state_enum.LightsailDistributionSubdomainStateEnum"
    """<p>The state of the subdomain for the distribution.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>Creating</code> – The subdomain is being created.</p> </li> <li> <p> <code>Attaching</code> – The subdomain is being associated with the distribution.</p> </li> <li> <p> <code>Attached</code> – The subdomain is associated with the distribution.</p> </li> <li> <p> <code>Error</code> – The subdomain couldn't be created or associated with the distribution. For more information, see the <code>errorCode</code> and <code>errorDetails</code> parameters.</p> </li> </ul>"""
    error_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The error code that describes why the subdomain is in the <code>Error</code> state.</p>"""
    error_details: NotRequired["capo_lightsail.types.string.string"]
    """<p>The details of the error that caused the subdomain to be in the <code>Error</code> state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LightsailDistributionSubdomain) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_lightsail.types.lightsail_distribution_subdomain_state_enum

    out["state"] = (
        capo_lightsail.types.lightsail_distribution_subdomain_state_enum.serialize_aws_json_1_1(
            value["state"]
        )
    )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LightsailDistributionSubdomain:
    out: LightsailDistributionSubdomain = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("state") is not None:
        import capo_lightsail.types.lightsail_distribution_subdomain_state_enum

        out["state"] = (
            capo_lightsail.types.lightsail_distribution_subdomain_state_enum.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_lightsail.types.lightsail_distribution_subdomain_state_enum.LightsailDistributionSubdomainStateEnum",
            "",
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorDetails") is not None:
        out["error_details"] = data["errorDetails"]
    return out
