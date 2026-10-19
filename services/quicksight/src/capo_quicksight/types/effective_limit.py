"""Generated from Smithy shape ``com.amazonaws.quicksight#EffectiveLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.effective_limit_limit_value_long
    import capo_quicksight.types.limit_source
    import capo_quicksight.types.limit_unit
    import capo_quicksight.types.profile_id
    import capo_quicksight.types.resource_type


class EffectiveLimit(TypedDict, closed=True):
    resource_type: "capo_quicksight.types.resource_type.ResourceType"
    """<p>The type of resource that the limit applies to.</p>"""
    limit_value: "capo_quicksight.types.effective_limit_limit_value_long.EffectiveLimitLimitValueLong"
    """<p>The maximum allowed value for the resource.</p>"""
    limit_unit: "capo_quicksight.types.limit_unit.LimitUnit"
    """<p>The unit of measurement for the limit.</p>"""
    source: "capo_quicksight.types.limit_source.LimitSource"
    """<p>The source from which this limit was inherited. Possible values:</p> <ul> <li> <p> <code>DIRECT_USER</code> – The limit comes from a profile directly assigned to the user.</p> </li> <li> <p> <code>GROUP</code> – The limit comes from a profile assigned to a group the user belongs to.</p> </li> <li> <p> <code>ROLE</code> – The limit comes from a profile assigned to a role the user has.</p> </li> <li> <p> <code>ACCOUNT</code> – The limit comes from the account-level default profile.</p> </li> <li> <p> <code>SYSTEM_DEFAULT</code> – The limit comes from the built-in system default.</p> </li> </ul>"""
    profile_id: "capo_quicksight.types.profile_id.ProfileId"
    """<p>The identifier of the limits profile that defines this limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveLimit) -> dict:
    out: dict = {}
    import capo_quicksight.types.resource_type

    out["resourceType"] = capo_quicksight.types.resource_type.serialize_json(
        value["resource_type"]
    )
    out["limitValue"] = value["limit_value"]
    import capo_quicksight.types.limit_unit

    out["limitUnit"] = capo_quicksight.types.limit_unit.serialize_json(
        value["limit_unit"]
    )
    import capo_quicksight.types.limit_source

    out["source"] = capo_quicksight.types.limit_source.serialize_json(value["source"])
    out["profileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> EffectiveLimit:
    out: EffectiveLimit = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_quicksight.types.resource_type

        out["resource_type"] = capo_quicksight.types.resource_type.deserialize_json(
            data["resourceType"]
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_quicksight.types.resource_type.ResourceType", ""
        )
    if data.get("limitValue") is not None:
        out["limit_value"] = data["limitValue"]
    else:
        out["limit_value"] = 0
    if data.get("limitUnit") is not None:
        import capo_quicksight.types.limit_unit

        out["limit_unit"] = capo_quicksight.types.limit_unit.deserialize_json(
            data["limitUnit"]
        )
    else:
        import typing

        out["limit_unit"] = typing.cast(
            "capo_quicksight.types.limit_unit.LimitUnit", ""
        )
    if data.get("source") is not None:
        import capo_quicksight.types.limit_source

        out["source"] = capo_quicksight.types.limit_source.deserialize_json(
            data["source"]
        )
    else:
        import typing

        out["source"] = typing.cast(
            "capo_quicksight.types.limit_source.LimitSource", ""
        )
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    return out
