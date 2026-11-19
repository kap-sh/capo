"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceIdScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_region
    import capo_observabilityadmin.types.azure_resource_id_list


class AzureResourceIdScope(TypedDict, closed=True):
    region: "capo_observabilityadmin.types.azure_region.AzureRegion"
    """<p>The Azure Region of the resources, for example <code>eastus</code>. Required because an Azure resource ID doesn't include the Region.</p>"""
    resource_ids: (
        "capo_observabilityadmin.types.azure_resource_id_list.AzureResourceIdList"
    )
    """<p>The Azure Resource Manager IDs of the resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceIdScope) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    import capo_observabilityadmin.types.azure_resource_id_list

    out["ResourceIds"] = (
        capo_observabilityadmin.types.azure_resource_id_list.serialize_json(
            value["resource_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> AzureResourceIdScope:
    out: AzureResourceIdScope = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("ResourceIds") is not None:
        import capo_observabilityadmin.types.azure_resource_id_list

        out["resource_ids"] = (
            capo_observabilityadmin.types.azure_resource_id_list.deserialize_json(
                data["ResourceIds"]
            )
        )
    else:
        out["resource_ids"] = []
    return out
