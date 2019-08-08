import logging
from collections import defaultdict
from typing import Dict


logger = logging.getLogger(__name__)


class EventManager:
    __subscribers: Dict = defaultdict(set)

    @classmethod
    def subscribe(cls, subscriber, event):
        cls.__subscribers[event].add(subscriber)

    @classmethod
    def trigger(cls, event):
        for subscriber in cls.__subscribers.get(event.__class__, []):
            subscriber(event)

    @classmethod
    def _reset(cls):
        """Never call this outside tests!"""
        cls.__subscribers = defaultdict(set)

    @classmethod
    def subscribers(cls) -> Dict:
        return dict(cls.__subscribers)
