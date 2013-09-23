# -*- coding:utf-8 -*-
__author__ = 'michael'


class NegotiationGroupMultifacetedView(TemplateView):
    ### TemplateResponseMixin
    template_name = 'offers/offer_detail.html'

    ### ContextMixin
    def get_context_data(self, **kwargs):
        """ Adds extra content to our template """
        context = super(NegotiationGroupDetailView, self).get_context_data(**kwargs)

        ...

        context['negotiation_bid_form'] = NegotiationBidForm(
            prefix='NegotiationBidForm',
            ...
            # Multiple 'submit' button paths should be handled in form's .save()/clean()
            data = self.request.POST if bool(set(['NegotiationBidForm-submit-counter-bid',
                                              'NegotiationBidForm-submit-approve-bid',
                                              'NegotiationBidForm-submit-decline-further-bids']).intersection(
                                                    self.request.POST)) else None,
            )
        context['offer_attachment_form'] = NegotiationAttachmentForm(
            prefix='NegotiationAttachment',
            ...
            data = self.request.POST if 'NegotiationAttachment-submit' in self.request.POST else None,
            files = self.request.FILES if 'NegotiationAttachment-submit' in self.request.POST else None
            )
        context['offer_contact_form'] = NegotiationContactForm()
        return context

    ### NegotiationGroupDetailView
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if context['negotiation_bid_form'].is_valid():
            instance = context['negotiation_bid_form'].save()
            messages.success(request, 'Your offer bid #{0} has been submitted.'.format(instance.pk))
        elif context['offer_attachment_form'].is_valid():
            instance = context['offer_attachment_form'].save()
            messages.success(request, 'Your offer attachment #{0} has been submitted.'.format(instance.pk))
                # advise of any errors

        else
            messages.error('Error(s) encountered during form processing, please review below and re-submit')

        return self.render_to_response(context)




<form id='offer_negotiation_form' class="content-form" action='./' enctype="multipart/form-data" method="post" accept-charset="utf-8">
    {% csrf_token %}
    {{ negotiation_bid_form.as_p }}
    ...
    <input type="submit" name="{{ negotiation_bid_form.prefix }}-submit-counter-bid"
    title="Submit a counter bid"
    value="Counter Bid" />
</form>

...

<form id='offer-attachment-form' class="content-form" action='./' enctype="multipart/form-data" method="post" accept-charset="utf-8">
    {% csrf_token %}
    {{ offer_attachment_form.as_p }}

    <input name="{{ offer_attachment_form.prefix }}-submit" type="submit" value="Submit" />
</form>
