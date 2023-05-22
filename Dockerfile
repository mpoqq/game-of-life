FROM alpine:3.17.3

# Install vector certificate
ADD https://vistradpart1.vi.vector.int/artifactory/adp-globaltools-generic-prod/Vector_Root_2.0.crt /usr/local/share/ca-certificates/vector_root.crt
ADD https://vistradpart1.vi.vector.int/artifactory/adp-globaltools-generic-prod/Vector_Issuing_2.0.crt /usr/local/share/ca-certificates/vector_issuing.crt

RUN cat /usr/local/share/ca-certificates/* >> /etc/ssl/cert.pem

RUN apk add --no-cache icu-libs

