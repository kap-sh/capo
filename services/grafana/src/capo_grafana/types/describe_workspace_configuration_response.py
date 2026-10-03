"""Generated from Smithy shape ``com.amazonaws.grafana#DescribeWorkspaceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.grafana_version
    import capo_grafana.types.overridable_configuration_json


class DescribeWorkspaceConfigurationResponse(TypedDict, closed=True):
    configuration: (
        "capo_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
    )
    """<p>The configuration string for the workspace that you requested. For more information about the format and configuration options available, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html">Working in your Grafana workspace</a>.</p>"""
    grafana_version: NotRequired["capo_grafana.types.grafana_version.GrafanaVersion"]
    """<p>The supported Grafana version for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceConfigurationResponse) -> dict:
    out: dict = {}
    out["configuration"] = value["configuration"]
    if "grafana_version" in value:
        out["grafanaVersion"] = value["grafana_version"]
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceConfigurationResponse:
    out: DescribeWorkspaceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError(
            "DescribeWorkspaceConfigurationResponse.configuration required"
        )
    if data.get("grafanaVersion") is not None:
        out["grafana_version"] = data["grafanaVersion"]
    return out
