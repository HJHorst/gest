import re
import logging

logging.basicConfig(level=logging.DEBUG)


class SepaSplitter:

    def split_kvp(self, doc, kvp):
        pair = kvp.split(':', 1)
        key = pair[0]
        logging.info('KEY %s', key)
        value = pair[1]
        if value.count('{') > 0:
            doc[key] = {}
            self.parse_structure(doc[key], value)
        elif value[0] == ':':
            doc[key] = {}
            self.parse_attributes(doc[key], value)
        else:
            doc[key] = value

    def parse_attributes(self, doc, attrs):
        # logging.debug('attr: %s', attrs)
        expr = re.compile(':[0-9A-Z]{2,3}:')
        attributes = expr.split(attrs)
        keys = expr.findall(attrs)
        logging.debug(len(keys))
        logging.debug(len(attributes))
        for index, key in enumerate(keys):
            key = key.strip(':')
            logging.debug(key + ' == ' + attributes[index + 1])
            doc[key] = attributes[index + 1].strip()

    def parse_structure(self, doc, structure):
        logging.debug('>> %s <<', structure[0:50])
        structure = structure.strip()
        logging.info('====== %s - %s', structure.count('{'), structure.count('}'))
        while len(structure) > 0 and structure[0] == '{':
            start = 1
            for (index, letter) in [(index, letter) for index, letter in enumerate(structure[1:]) if letter in '{}']:
                if letter == '{':
                    start += 1
                if letter == '}':
                    start -= 1
                    if start == 0:
                        logging.debug('end on %s: %s', index, letter)
                        logging.info('KVP: %s', structure[1:index+1])
                        self.split_kvp(doc, structure[1:index+1])
                        structure = structure[index+2:].strip()
                        logging.debug('REST %s', structure[0:40])
                        break

    def parse_document(self, lines):
        doc = {}
        # logging.info('document')
        header = True
        structured = '';
        for index, line in enumerate(lines):
            if index == 0:
                logging.info(line.strip())
            elif len(line) > 0:
                if line[0] == '{':
                    header = False
                if header:
                    # parse_line(doc, line)
                    pass
                else:
                    structured += line
                    # self.parse_structured(doc, line)
        self.parse_structure(doc, structured)
        logging.info(doc)
        return doc

    def write_document(self, lines):
        # logging.info('write')
        # document = open(str(uuid.uuid4()) + '.txt', 'w')
        # document.writelines(lines)
        doc = self.parse_document(lines)
        x = '3.103'
        logging.info(self.get_dot_value(doc, x))
        tags = [['BEDRAG', '4.33B', '[3:]'], ['VALUTA', '4.33B', '[0:3]'], ['IBAN', '4.50K', '.split(''\n'')[0][1:]']]
        logging.info(self.create_xml(doc, tags))

    def create_xml(self, doc, tags):
        xml = ''
        for tag in tags:
            val = self.get_dot_value(doc, tag[1])
            if len(tag) == 3:
                logging.debug('==>%s', val+tag[2])
                val = eval('val'+tag[2])
            xml += '<'+tag[0]+'>'+val+'</'+tag[0]+'>'
        return xml

    def get_dot_value(self, doc, dotexpr):
        attrs = dotexpr.split('.')
        return self.get_value(doc, attrs)

    def get_value(self, doc, attrs):
        if len(attrs) > 1:
            return self.get_value(doc[attrs[0]], attrs[1:])
        else:
            return doc[attrs[0]]

    def process_file(self, filename):
        lines = []
        f = open(filename, 'r')

        for line in f:
            # logging.info(line)
            tags = re.findall('\f', line, 0)
            if len(tags) > 0:
                logging.info('change after' + str(len(lines)))
                self.write_document(lines)
                break
                lines = [line]
            else:
                lines.append(line)


if __name__ == '__main__':
    sp = SepaSplitter()
    sp.process_file('PAGE0.txt')
