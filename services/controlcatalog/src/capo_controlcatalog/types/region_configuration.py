"""Generated from Smithy shape ``com.amazonaws.controlcatalog#RegionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.control_scope
    import capo_controlcatalog.types.deployable_regions


class RegionConfiguration(TypedDict, closed=True):
    scope: "capo_controlcatalog.types.control_scope.ControlScope"
    """<p>The coverage of the control, if deployed. Scope is an enumerated type, with value <code>Regional</code>, or <code>Global</code>. A control with Global scope is effective in all Amazon Web Services Regions, regardless of the Region from which it is enabled, or to which it is deployed. A control implemented by an SCP is usually Global in scope. A control with Regional scope has operations that are restricted specifically to the Region from which it is enabled and to which it is deployed. Controls implemented by Config rules and CloudFormation hooks usually are Regional in scope. Security Hub controls usually are Regional in scope.</p>"""
    deployable_regions: NotRequired[
        "capo_controlcatalog.types.deployable_regions.DeployableRegions"
    ]
    """<p>Regions in which the control is available to be deployed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionConfiguration) -> dict:
    out: dict = {}
    import capo_controlcatalog.types.control_scope

    out["Scope"] = capo_controlcatalog.types.control_scope.serialize_json(
        value["scope"]
    )
    if "deployable_regions" in value:
        import capo_controlcatalog.types.deployable_regions

        out["DeployableRegions"] = (
            capo_controlcatalog.types.deployable_regions.serialize_json(
                value["deployable_regions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegionConfiguration:
    out: RegionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_controlcatalog.types.control_scope

        out["scope"] = capo_controlcatalog.types.control_scope.deserialize_json(
            data["Scope"]
        )
    else:
        import typing

        out["scope"] = typing.cast(
            "capo_controlcatalog.types.control_scope.ControlScope", ""
        )
    if data.get("DeployableRegions") is not None:
        import capo_controlcatalog.types.deployable_regions

        out["deployable_regions"] = (
            capo_controlcatalog.types.deployable_regions.deserialize_json(
                data["DeployableRegions"]
            )
        )
    return out
