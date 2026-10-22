"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_attribute_key
    import capo_network_firewall.types.container_attribute_value


class ContainerAttribute(TypedDict, closed=True):
    key: "capo_network_firewall.types.container_attribute_key.ContainerAttributeKey"
    """<p>The attribute key to filter on. For Amazon EKS, specify <code>namespace</code> to filter by namespace, or specify a Kubernetes label key. For Amazon ECS, specify a container instance attribute name. Keys don't support wildcards.</p> <p>Valid characters are letters, numbers, spaces, hyphens (<code>-</code>), underscores (<code>_</code>), periods (<code>.</code>), forward slashes (<code>/</code>), and colons (<code>:</code>).</p>"""
    value: (
        "capo_network_firewall.types.container_attribute_value.ContainerAttributeValue"
    )
    r"""<p>The attribute value to match. You can specify an exact value, such as <code>payments-api</code>, or a wildcard pattern, such as <code>payments-*</code>.</p> <p>Valid characters are letters, numbers, spaces, hyphens (<code>-</code>), underscores (<code>_</code>), periods (<code>.</code>), forward slashes (<code>/</code>), colons (<code>:</code>), asterisks (<code>*</code>), and backslashes (<code>\</code>).</p> <p>Network Firewall evaluates the value using the following rules:</p> <ul> <li> <p>An asterisk (<code>*</code>) matches zero or more characters. For example, <code>payments-*</code> matches <code>payments-</code>, <code>payments-api</code>, and <code>payments-api-v2</code>, and <code>*-prod</code> matches <code>web-prod</code>.</p> </li> <li> <p>The pattern must match the entire value. For example, <code>payments-*</code> doesn't match <code>my-payments-api</code>. To match a value that contains <code>payments</code> anywhere, use <code>*payments*</code>.</p> </li> <li> <p>Matching is case sensitive. For example, <code>Payments-*</code> doesn't match <code>payments-api</code>.</p> </li> <li> <p>To match a literal asterisk, escape it with a backslash (<code>\*</code>). To match a literal backslash, use <code>\\</code>. A backslash followed by any other character matches a literal backslash followed by that character.</p> </li> <li> <p>A wildcard pattern matches only containers that have the attribute. For example, a filter with key <code>app</code> and value <code>*</code> matches every container that has an <code>app</code> label, but doesn't match a container without an <code>app</code> label.</p> </li> <li> <p>A value that doesn't contain <code>*</code> or <code>\</code> matches only that exact value.</p> </li> </ul> <p>A value can contain at most 10 unescaped asterisks. Escaped asterisks (<code>\*</code>) don't count toward this limit. A value can't end with a single unescaped backslash.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContainerAttribute:
    out: ContainerAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
