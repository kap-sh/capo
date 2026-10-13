"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptPredictionsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.accept_choices
    import capo_datazone.types.accept_rule
    import capo_datazone.types.asset_identifier
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.revision


class AcceptPredictionsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    identifier: "capo_datazone.types.asset_identifier.AssetIdentifier"
    """<p>The identifier of the asset.</p>"""
    revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision that is to be made to the asset.</p>"""
    accept_rule: NotRequired["capo_datazone.types.accept_rule.AcceptRule"]
    """<p>Specifies the rule (or the conditions) under which a prediction can be accepted.</p>"""
    accept_choices: NotRequired["capo_datazone.types.accept_choices.AcceptChoices"]
    """<p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be accepted.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptPredictionsInput) -> dict:
    out: dict = {}
    if "accept_rule" in value:
        import capo_datazone.types.accept_rule

        out["acceptRule"] = capo_datazone.types.accept_rule.serialize_json(
            value["accept_rule"]
        )
    if "accept_choices" in value:
        import capo_datazone.types.accept_choices

        out["acceptChoices"] = capo_datazone.types.accept_choices.serialize_json(
            value["accept_choices"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AcceptPredictionsInput:
    out: AcceptPredictionsInput = {}  # type: ignore[typeddict-item]
    if data.get("acceptRule") is not None:
        import capo_datazone.types.accept_rule

        out["accept_rule"] = capo_datazone.types.accept_rule.deserialize_json(
            data["acceptRule"]
        )
    if data.get("acceptChoices") is not None:
        import capo_datazone.types.accept_choices

        out["accept_choices"] = capo_datazone.types.accept_choices.deserialize_json(
            data["acceptChoices"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: AcceptPredictionsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accept_choices" in value:
        import capo_datazone.types.accept_choices

        out["accept_choices"] = capo_datazone.types.accept_choices.redact_sensitive(
            value["accept_choices"]
        )
    return out
