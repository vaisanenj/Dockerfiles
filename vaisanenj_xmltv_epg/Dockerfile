FROM python:3.9-slim

#Update and install necessary packages.
RUN apt-get update && \
    apt-get install -y wget &&  \
    apt-get install -y xmltv

#Change user that jellyfin instance uses
USER 1001:3004

#Create workdir
WORKDIR /EPG

COPY get_epg.sh /EPG
COPY tv_grab.conf /EPG
COPY edit_epg.py /EPG

#Volume where EPG is stored
VOLUME /output


ENTRYPOINT ["./get_epg.sh"]