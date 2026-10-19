"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCisTargets``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.target_account_list
    import capo_inspector2.types.target_resource_tags


class CreateCisTargets(TypedDict, closed=True):
    account_ids: "capo_inspector2.types.target_account_list.TargetAccountList"
    """<p>The CIS target account ids.</p>"""
    target_resource_tags: (
        "capo_inspector2.types.target_resource_tags.TargetResourceTags"
    )
    """<p>The CIS target resource tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCisTargets) -> dict:
    out: dict = {}
    import capo_inspector2.types.target_account_list

    out["accountIds"] = capo_inspector2.types.target_account_list.serialize_json(
        value["account_ids"]
    )
    import capo_inspector2.types.target_resource_tags

    out["targetResourceTags"] = (
        capo_inspector2.types.target_resource_tags.serialize_json(
            value["target_resource_tags"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCisTargets:
    out: CreateCisTargets = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_inspector2.types.target_account_list

        out["account_ids"] = capo_inspector2.types.target_account_list.deserialize_json(
            data["accountIds"]
        )
    else:
        out["account_ids"] = []
    if data.get("targetResourceTags") is not None:
        import capo_inspector2.types.target_resource_tags

        out["target_resource_tags"] = (
            capo_inspector2.types.target_resource_tags.deserialize_json(
                data["targetResourceTags"]
            )
        )
    else:
        out["target_resource_tags"] = {}
    return out
