import graphene
from graphql_jwt.decorators import login_required

from .types import EventType
from .models import Event

class AddEvent(graphene.Mutation):
    # The class attributes define the response of the mutation
    event = graphene.Field(EventType)

    class Arguments:
        # The input arguments for this mutation
        url = graphene.String(required=True)
        name = graphene.String()

    @login_required
    def mutate(self, info, **kwargs):
        _event = Event.objects.create(**kwargs)

        # Notice we return an instance of this mutation
        return AddEvent(event=_event)


class Query(object):
    all_events = graphene.List(EventType, limit=graphene.Int())

    def resolve_all_events(self, info, limit=None, **kwargs):
        return Event.objects.all()[:limit]

class Mutation(object):
    add_event = AddEvent.Field()