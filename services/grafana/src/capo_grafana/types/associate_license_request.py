"""Generated from Smithy shape ``com.amazonaws.grafana#AssociateLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.grafana_token
    import capo_grafana.types.license_type
    import capo_grafana.types.workspace_id


class AssociateLicenseRequest(TypedDict, closed=True):
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to associate the license with.</p>"""
    license_type: "capo_grafana.types.license_type.LicenseType"
    """<p>The type of license to associate with the workspace.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>"""
    grafana_token: NotRequired["capo_grafana.types.grafana_token.GrafanaToken"]
    """<p>A token from Grafana Labs that ties your Amazon Web Services account with a Grafana Labs account. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise">Link your account with Grafana Labs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLicenseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateLicenseRequest:
    out: AssociateLicenseRequest = {}  # type: ignore[typeddict-item]
    return out
