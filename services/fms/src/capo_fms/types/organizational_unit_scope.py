"""Generated from Smithy shape ``com.amazonaws.fms#OrganizationalUnitScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.organizational_unit_id_list


class OrganizationalUnitScope(TypedDict, closed=True):
    organizational_units: NotRequired[
        "capo_fms.types.organizational_unit_id_list.OrganizationalUnitIdList"
    ]
    """<p>The list of OUs within the organization that the specified Firewall Manager administrator either can or cannot apply policies to, based on the value of <code>OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits</code>. If <code>OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits</code> is set to <code>true</code>, then the Firewall Manager administrator can apply policies to all OUs in the organization except for the OUs in this list. If <code>OrganizationalUnitScope$ExcludeSpecifiedOrganizationalUnits</code> is set to <code>false</code>, then the Firewall Manager administrator can only apply policies to the OUs in this list.</p>"""
    all_organizational_units_enabled: "capo_fms.types.boolean.Boolean"
    """<p>A boolean value that indicates if the administrator can apply policies to all OUs within an organization. If true, the administrator can manage all OUs within the organization. You can either enable management of all OUs through this operation, or you can specify OUs to manage in <code>OrganizationalUnitScope$OrganizationalUnits</code>. You cannot specify both.</p>"""
    exclude_specified_organizational_units: "capo_fms.types.boolean.Boolean"
    """<p>A boolean value that excludes the OUs in <code>OrganizationalUnitScope$OrganizationalUnits</code> from the administrator's scope. If true, the Firewall Manager administrator can apply policies to all OUs in the organization except for the OUs listed in <code>OrganizationalUnitScope$OrganizationalUnits</code>. You can either specify a list of OUs to exclude by <code>OrganizationalUnitScope$OrganizationalUnits</code>, or you can enable management of all OUs by <code>OrganizationalUnitScope$AllOrganizationalUnitsEnabled</code>. You cannot specify both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnitScope) -> dict:
    out: dict = {}
    if "organizational_units" in value:
        import capo_fms.types.organizational_unit_id_list

        out["OrganizationalUnits"] = (
            capo_fms.types.organizational_unit_id_list.serialize_aws_json_1_1(
                value["organizational_units"]
            )
        )
    out["AllOrganizationalUnitsEnabled"] = value.get(
        "all_organizational_units_enabled", False
    )
    out["ExcludeSpecifiedOrganizationalUnits"] = value.get(
        "exclude_specified_organizational_units", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationalUnitScope:
    out: OrganizationalUnitScope = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationalUnits") is not None:
        import capo_fms.types.organizational_unit_id_list

        out["organizational_units"] = (
            capo_fms.types.organizational_unit_id_list.deserialize_aws_json_1_1(
                data["OrganizationalUnits"]
            )
        )
    if data.get("AllOrganizationalUnitsEnabled") is not None:
        out["all_organizational_units_enabled"] = data["AllOrganizationalUnitsEnabled"]
    else:
        out["all_organizational_units_enabled"] = False
    if data.get("ExcludeSpecifiedOrganizationalUnits") is not None:
        out["exclude_specified_organizational_units"] = data[
            "ExcludeSpecifiedOrganizationalUnits"
        ]
    else:
        out["exclude_specified_organizational_units"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OrganizationalUnitScope) -> dict:
    out: dict = {}
    if "organizational_units" in value:
        import capo_fms.types.organizational_unit_id_list

        out["OrganizationalUnits"] = (
            capo_fms.types.organizational_unit_id_list.serialize_cbor(
                value["organizational_units"]
            )
        )
    out["AllOrganizationalUnitsEnabled"] = value.get(
        "all_organizational_units_enabled", False
    )
    out["ExcludeSpecifiedOrganizationalUnits"] = value.get(
        "exclude_specified_organizational_units", False
    )
    return out


def deserialize_cbor(data: dict) -> OrganizationalUnitScope:
    out: OrganizationalUnitScope = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationalUnits") is not None:
        import capo_fms.types.organizational_unit_id_list

        out["organizational_units"] = (
            capo_fms.types.organizational_unit_id_list.deserialize_cbor(
                data["OrganizationalUnits"]
            )
        )
    if data.get("AllOrganizationalUnitsEnabled") is not None:
        out["all_organizational_units_enabled"] = data["AllOrganizationalUnitsEnabled"]
    else:
        out["all_organizational_units_enabled"] = False
    if data.get("ExcludeSpecifiedOrganizationalUnits") is not None:
        out["exclude_specified_organizational_units"] = data[
            "ExcludeSpecifiedOrganizationalUnits"
        ]
    else:
        out["exclude_specified_organizational_units"] = False
    return out
