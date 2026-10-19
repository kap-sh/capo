"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_version_filter_key
    import capo_launch_wizard.types.deployment_pattern_version_filter_values


class DeploymentPatternVersionFilter(TypedDict, closed=True):
    name: "capo_launch_wizard.types.deployment_pattern_version_filter_key.DeploymentPatternVersionFilterKey"
    """<p>The name of the filter attribute. Specifies which attribute to filter on when querying deployment pattern versions.</p>"""
    values: "capo_launch_wizard.types.deployment_pattern_version_filter_values.DeploymentPatternVersionFilterValues"
    """<p>The values to filter by. Contains the specific values to match against when filtering deployment pattern versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPatternVersionFilter) -> dict:
    out: dict = {}
    import capo_launch_wizard.types.deployment_pattern_version_filter_key

    out["name"] = (
        capo_launch_wizard.types.deployment_pattern_version_filter_key.serialize_json(
            value["name"]
        )
    )
    import capo_launch_wizard.types.deployment_pattern_version_filter_values

    out["values"] = (
        capo_launch_wizard.types.deployment_pattern_version_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeploymentPatternVersionFilter:
    out: DeploymentPatternVersionFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_launch_wizard.types.deployment_pattern_version_filter_key

        out["name"] = (
            capo_launch_wizard.types.deployment_pattern_version_filter_key.deserialize_json(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_launch_wizard.types.deployment_pattern_version_filter_key.DeploymentPatternVersionFilterKey",
            "",
        )
    if data.get("values") is not None:
        import capo_launch_wizard.types.deployment_pattern_version_filter_values

        out["values"] = (
            capo_launch_wizard.types.deployment_pattern_version_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
