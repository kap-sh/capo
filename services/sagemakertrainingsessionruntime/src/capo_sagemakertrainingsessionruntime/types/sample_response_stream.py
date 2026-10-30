"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleResponseStream``."""

from typing import TypeAlias

from capo_sagemakertrainingsessionruntime._iter import AnyIterator

"""<p>The streaming response body, delivered as Server-Sent Events (<code>text/event-stream</code>). Each event is a <code>data: {JSON}</code> line containing a chat completion chunk, and the stream is terminated by <code>data: [DONE]</code>. If an error occurs after streaming has started, it is delivered as a <code>data: {"error": {...}}</code> event and the stream ends without a <code>[DONE]</code> marker. Errors that occur before streaming starts are returned as the operation's errors.</p>"""
SampleResponseStream: TypeAlias = AnyIterator[bytes]
