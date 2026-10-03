"""Generated from Smithy shape ``com.amazonaws.grafana#NetworkAccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.prefix_list_ids
    import capo_grafana.types.vpce_ids


class NetworkAccessConfiguration(TypedDict, closed=True):
    prefix_list_ids: "capo_grafana.types.prefix_list_ids.PrefixListIds"
    """<p>An array of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration (passed an empty array) then no IP addresses are allowed to access the workspace. You create a prefix list using the Amazon VPC console.</p> <p>Prefix list IDs have the format <code>pl-<i>1a2b3c4d</i> </code>.</p> <p>For more information about prefix lists, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html">Group CIDR blocks using managed prefix lists</a>in the <i>Amazon Virtual Private Cloud User Guide</i>.</p>"""
    vpce_ids: "capo_grafana.types.vpce_ids.VpceIds"
    """<p>An array of Amazon VPC endpoint IDs for the workspace. You can create VPC endpoints to your Amazon Managed Grafana workspace for access from within a VPC. If a <code>NetworkAccessConfiguration</code> is specified then only VPC endpoints specified here are allowed to access the workspace. If you pass in an empty array of strings, then no VPCs are allowed to access the workspace.</p> <p>VPC endpoint IDs have the format <code>vpce-<i>1a2b3c4d</i> </code>.</p> <p>For more information about creating an interface VPC endpoint, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/VPC-endpoints">Interface VPC endpoints</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> <note> <p>The only VPC endpoints that can be specified here are interface VPC endpoints for Grafana workspaces (using the <code>com.amazonaws.[region].grafana-workspace</code> service endpoint). Other VPC endpoints are ignored.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAccessConfiguration) -> dict:
    out: dict = {}
    import capo_grafana.types.prefix_list_ids

    out["prefixListIds"] = capo_grafana.types.prefix_list_ids.serialize_json(
        value["prefix_list_ids"]
    )
    import capo_grafana.types.vpce_ids

    out["vpceIds"] = capo_grafana.types.vpce_ids.serialize_json(value["vpce_ids"])
    return out


def deserialize_json(data: dict) -> NetworkAccessConfiguration:
    out: NetworkAccessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("prefixListIds") is not None:
        import capo_grafana.types.prefix_list_ids

        out["prefix_list_ids"] = capo_grafana.types.prefix_list_ids.deserialize_json(
            data["prefixListIds"]
        )
    else:
        raise DeserializationError(
            "NetworkAccessConfiguration.prefix_list_ids required"
        )
    if data.get("vpceIds") is not None:
        import capo_grafana.types.vpce_ids

        out["vpce_ids"] = capo_grafana.types.vpce_ids.deserialize_json(data["vpceIds"])
    else:
        raise DeserializationError("NetworkAccessConfiguration.vpce_ids required")
    return out
