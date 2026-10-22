"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RetrievalInstructionFieldName``."""

from typing import Literal, TypeAlias, cast

"""<p>Identifies one field of RetrievalInstructionContent:</p> <ul> <li> <p>RETRIEVAL_GUIDANCE – retrievalGuidance</p> </li> <li> <p>PERSONA – persona</p> </li> <li> <p>ANSWER_FORMAT – answerFormat</p> </li> <li> <p>ANSWER_POLICY – answerPolicy</p> </li> </ul>"""
RetrievalInstructionFieldName: TypeAlias = Literal[
    "RETRIEVAL_GUIDANCE",
    "PERSONA",
    "ANSWER_FORMAT",
    "ANSWER_POLICY",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalInstructionFieldName) -> str:
    return value


def deserialize_json(data: str) -> RetrievalInstructionFieldName:
    return cast(RetrievalInstructionFieldName, data)
