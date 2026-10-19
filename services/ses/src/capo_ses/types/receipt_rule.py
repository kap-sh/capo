"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.enabled
    import capo_ses.types.receipt_actions_list
    import capo_ses.types.receipt_rule_name
    import capo_ses.types.recipients_list
    import capo_ses.types.tls_policy


class ReceiptRule(TypedDict, closed=True):
    name: "capo_ses.types.receipt_rule_name.ReceiptRuleName"
    """<p>The name of the receipt rule. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or periods (.). </p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""
    enabled: "capo_ses.types.enabled.Enabled"
    """<p>If <code>true</code>, the receipt rule is active. The default value is <code>false</code>.</p>"""
    tls_policy: NotRequired["capo_ses.types.tls_policy.TlsPolicy"]
    """<p>Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to <code>Require</code>, Amazon SES bounces emails that are not received over TLS. The default is <code>Optional</code>.</p>"""
    recipients: NotRequired["capo_ses.types.recipients_list.RecipientsList"]
    """<p>The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule matches all recipients on all verified domains.</p>"""
    actions: NotRequired["capo_ses.types.receipt_actions_list.ReceiptActionsList"]
    """<p>An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.</p>"""
    scan_enabled: "capo_ses.types.enabled.Enabled"
    """<p>If <code>true</code>, then messages that this receipt rule applies to are scanned for spam and viruses. The default value is <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    pairs.append(
        (f"{key_prefix}Enabled", "true" if value.get("enabled", False) else "false")
    )
    if "tls_policy" in value:
        import capo_ses.types.tls_policy

        capo_ses.types.tls_policy.serialize_query(
            value["tls_policy"], pairs, f"{key_prefix}TlsPolicy"
        )
    if "recipients" in value:
        import capo_ses.types.recipients_list

        capo_ses.types.recipients_list.serialize_query(
            value["recipients"], pairs, f"{key_prefix}Recipients"
        )
    if "actions" in value:
        import capo_ses.types.receipt_actions_list

        capo_ses.types.receipt_actions_list.serialize_query(
            value["actions"], pairs, f"{key_prefix}Actions"
        )
    pairs.append(
        (
            f"{key_prefix}ScanEnabled",
            "true" if value.get("scan_enabled", False) else "false",
        )
    )


def deserialize_query(el: Element) -> ReceiptRule:
    out: ReceiptRule = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_tls_policy = el.find("TlsPolicy")
    if child_tls_policy is not None:
        import capo_ses.types.tls_policy

        out["tls_policy"] = capo_ses.types.tls_policy.deserialize_query(
            child_tls_policy
        )
    child_recipients = el.find("Recipients")
    if child_recipients is not None:
        import capo_ses.types.recipients_list

        out["recipients"] = capo_ses.types.recipients_list.deserialize_query(
            child_recipients
        )
    child_actions = el.find("Actions")
    if child_actions is not None:
        import capo_ses.types.receipt_actions_list

        out["actions"] = capo_ses.types.receipt_actions_list.deserialize_query(
            child_actions
        )
    child_scan_enabled = el.find("ScanEnabled")
    if child_scan_enabled is not None:
        out["scan_enabled"] = (child_scan_enabled.text or "").lower() == "true"
    else:
        out["scan_enabled"] = False
    return out
