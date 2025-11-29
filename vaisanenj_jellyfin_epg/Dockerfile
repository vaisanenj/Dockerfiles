FROM python:3.9-slim

ENV COUNTRY="FI"

#Update and install necessary packages.
RUN apt-get update && \
    apt-get install -y wget

#Change user that jellyfin instance uses
USER 1001:3004

#Create workdir
WORKDIR /EPG

COPY get_epg.sh /EPG
COPY edit_xml.py /EPG

#Volume where EPG is stored
VOLUME /output

ENTRYPOINT ["./get_epg.sh"]