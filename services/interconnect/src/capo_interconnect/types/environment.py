"""Generated from Smithy shape ``com.amazonaws.interconnect#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_interconnect.types.bandwidths
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.environment_state
    import capo_interconnect.types.location
    import capo_interconnect.types.product_type
    import capo_interconnect.types.provider
    import capo_interconnect.types.remote_account_identifier_type


class Environment(TypedDict, closed=True):
    provider: "capo_interconnect.types.provider.Provider"
    """<p>The provider on the remote side of this <a>Connection</a>.</p>"""
    location: "capo_interconnect.types.location.Location"
    """<p>The provider specific location on the remote side of this <a>Connection</a>.</p>"""
    environment_id: "capo_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of this <a>Environment</a> </p>"""
    state: "capo_interconnect.types.environment_state.EnvironmentState"
    """<p>The state of the <a>Environment</a>. Possible values:</p> <ul> <li> <p> <code>available</code>: The environment is available and new <a>Connection</a> objects can be requested.</p> </li> <li> <p> <code>limited</code>: The environment is available, but overall capacity is limited. The set of available bandwidths </p> </li> <li> <p> <code>unavailable</code>: The environment is currently unavailable.</p> </li> </ul>"""
    bandwidths: "capo_interconnect.types.bandwidths.Bandwidths"
    """<p>The sets of bandwidths that are available and supported on this environment.</p>"""
    type: "capo_interconnect.types.product_type.ProductType"
    """<p>The specific product type of <a>Connection</a> objects provided by this <a>Environment</a>.</p>"""
    activation_page_url: NotRequired["str"]
    """<p>An HTTPS URL on the remote partner portal where the Activation Key should be brought to complete the creation process.</p>"""
    remote_identifier_type: NotRequired[
        "capo_interconnect.types.remote_account_identifier_type.RemoteAccountIdentifierType"
    ]
    """<p>The type of identifying information that should be supplied to the <code>remoteAccount</code> parameter of a <a>CreateConnection</a> call for this specific Environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Environment) -> dict:
    out: dict = {}
    import capo_interconnect.types.provider

    out["provider"] = capo_interconnect.types.provider.serialize_aws_json_1_0(
        value["provider"]
    )
    out["location"] = value["location"]
    out["environmentId"] = value["environment_id"]
    import capo_interconnect.types.environment_state

    out["state"] = capo_interconnect.types.environment_state.serialize_aws_json_1_0(
        value["state"]
    )
    import capo_interconnect.types.bandwidths

    out["bandwidths"] = capo_interconnect.types.bandwidths.serialize_aws_json_1_0(
        value["bandwidths"]
    )
    out["type"] = value["type"]
    if "activation_page_url" in value:
        out["activationPageUrl"] = value["activation_page_url"]
    if "remote_identifier_type" in value:
        import capo_interconnect.types.remote_account_identifier_type

        out["remoteIdentifierType"] = (
            capo_interconnect.types.remote_account_identifier_type.serialize_aws_json_1_0(
                value["remote_identifier_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    else:
        import capo_interconnect.types._unknown

        out["provider"] = capo_interconnect.types._unknown.UnknownUnionMember("")
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("state") is not None:
        import capo_interconnect.types.environment_state

        out["state"] = (
            capo_interconnect.types.environment_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_interconnect.types.environment_state.EnvironmentState", ""
        )
    if data.get("bandwidths") is not None:
        import capo_interconnect.types.bandwidths

        out["bandwidths"] = capo_interconnect.types.bandwidths.deserialize_aws_json_1_0(
            data["bandwidths"]
        )
    else:
        raise DeserializationError("Environment.bandwidths required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("activationPageUrl") is not None:
        out["activation_page_url"] = data["activationPageUrl"]
    if data.get("remoteIdentifierType") is not None:
        import capo_interconnect.types.remote_account_identifier_type

        out["remote_identifier_type"] = (
            capo_interconnect.types.remote_account_identifier_type.deserialize_aws_json_1_0(
                data["remoteIdentifierType"]
            )
        )
    return out
