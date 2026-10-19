"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkRecoveryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.start_source_network_recovery_request_network_entries
    import capo_drs.types.tags_map


class StartSourceNetworkRecoveryRequest(TypedDict, closed=True):
    source_networks: "capo_drs.types.start_source_network_recovery_request_network_entries.StartSourceNetworkRecoveryRequestNetworkEntries"
    """<p>The Source Networks that we want to start a Recovery Job for.</p>"""
    deploy_as_new: NotRequired["bool"]
    """<p>Don't update existing CloudFormation Stack, recover the network using a new stack.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags to be associated with the Source Network recovery Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkRecoveryRequest) -> dict:
    out: dict = {}
    import capo_drs.types.start_source_network_recovery_request_network_entries

    out["sourceNetworks"] = (
        capo_drs.types.start_source_network_recovery_request_network_entries.serialize_json(
            value["source_networks"]
        )
    )
    if "deploy_as_new" in value:
        out["deployAsNew"] = value["deploy_as_new"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartSourceNetworkRecoveryRequest:
    out: StartSourceNetworkRecoveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceNetworks") is not None:
        import capo_drs.types.start_source_network_recovery_request_network_entries

        out["source_networks"] = (
            capo_drs.types.start_source_network_recovery_request_network_entries.deserialize_json(
                data["sourceNetworks"]
            )
        )
    else:
        out["source_networks"] = []
    if data.get("deployAsNew") is not None:
        out["deploy_as_new"] = data["deployAsNew"]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartSourceNetworkRecoveryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_networks" in value:
        import capo_drs.types.start_source_network_recovery_request_network_entries

        out["source_networks"] = (
            capo_drs.types.start_source_network_recovery_request_network_entries.redact_sensitive(
                value["source_networks"]
            )
        )
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
