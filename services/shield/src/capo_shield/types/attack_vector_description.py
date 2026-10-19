"""Generated from Smithy shape ``com.amazonaws.shield#AttackVectorDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.string


class AttackVectorDescription(TypedDict, closed=True):
    vector_type: "capo_shield.types.string.String"
    """<p>The attack type. Valid values:</p> <ul> <li> <p>UDP_TRAFFIC</p> </li> <li> <p>UDP_FRAGMENT</p> </li> <li> <p>GENERIC_UDP_REFLECTION</p> </li> <li> <p>DNS_REFLECTION</p> </li> <li> <p>NTP_REFLECTION</p> </li> <li> <p>CHARGEN_REFLECTION</p> </li> <li> <p>SSDP_REFLECTION</p> </li> <li> <p>PORT_MAPPER</p> </li> <li> <p>RIP_REFLECTION</p> </li> <li> <p>SNMP_REFLECTION</p> </li> <li> <p>MSSQL_REFLECTION</p> </li> <li> <p>NET_BIOS_REFLECTION</p> </li> <li> <p>SYN_FLOOD</p> </li> <li> <p>ACK_FLOOD</p> </li> <li> <p>REQUEST_FLOOD</p> </li> <li> <p>HTTP_REFLECTION</p> </li> <li> <p>UDS_REFLECTION</p> </li> <li> <p>MEMCACHED_REFLECTION</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVectorDescription) -> dict:
    out: dict = {}
    out["VectorType"] = value["vector_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackVectorDescription:
    out: AttackVectorDescription = {}  # type: ignore[typeddict-item]
    if data.get("VectorType") is not None:
        out["vector_type"] = data["VectorType"]
    else:
        out["vector_type"] = ""
    return out
