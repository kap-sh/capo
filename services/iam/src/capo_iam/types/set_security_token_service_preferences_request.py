"""Generated from Smithy shape ``com.amazonaws.iam#SetSecurityTokenServicePreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.global_endpoint_token_version


class SetSecurityTokenServicePreferencesRequest(TypedDict, closed=True):
    global_endpoint_token_version: (
        "capo_iam.types.global_endpoint_token_version.globalEndpointTokenVersion"
    )
    """<p>The version of the global endpoint token. Version 1 tokens are valid only in Amazon Web Services Regions that are available by default. These tokens do not work in manually enabled Regions, such as Asia Pacific (Hong Kong). Version 2 tokens are valid in all Regions. However, version 2 tokens are longer and might affect systems where you temporarily store tokens.</p> <p>For information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html">Activating and deactivating STS in an Amazon Web Services Region</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSecurityTokenServicePreferencesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.global_endpoint_token_version

    capo_iam.types.global_endpoint_token_version.serialize_query(
        value["global_endpoint_token_version"],
        pairs,
        f"{key_prefix}GlobalEndpointTokenVersion",
    )


def deserialize_query(el: Element) -> SetSecurityTokenServicePreferencesRequest:
    out: SetSecurityTokenServicePreferencesRequest = {}  # type: ignore[typeddict-item]
    child_global_endpoint_token_version = el.find("GlobalEndpointTokenVersion")
    if child_global_endpoint_token_version is not None:
        import capo_iam.types.global_endpoint_token_version

        out["global_endpoint_token_version"] = (
            capo_iam.types.global_endpoint_token_version.deserialize_query(
                child_global_endpoint_token_version
            )
        )
    else:
        raise DeserializationError(
            "SetSecurityTokenServicePreferencesRequest.global_endpoint_token_version required"
        )
    return out
