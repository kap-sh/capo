"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.service_network_name
    import capo_vpc_lattice.types.sharing_config
    import capo_vpc_lattice.types.tag_map


class CreateServiceNetworkRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    name: "capo_vpc_lattice.types.service_network_name.ServiceNetworkName"
    """<p>The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    auth_type: NotRequired["capo_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the service network.</p>"""
    sharing_config: NotRequired["capo_vpc_lattice.types.sharing_config.SharingConfig"]
    """<p>Specify if the service network should be enabled for sharing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    if "sharing_config" in value:
        import capo_vpc_lattice.types.sharing_config

        out["sharingConfig"] = capo_vpc_lattice.types.sharing_config.serialize_json(
            value["sharing_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkRequest:
    out: CreateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("authType") is not None:
        out["auth_type"] = data["authType"]
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    if data.get("sharingConfig") is not None:
        import capo_vpc_lattice.types.sharing_config

        out["sharing_config"] = capo_vpc_lattice.types.sharing_config.deserialize_json(
            data["sharingConfig"]
        )
    return out
