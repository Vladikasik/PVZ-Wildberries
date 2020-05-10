# ---------------- #
try:
    # ---------------- #
    import json
    import socket
    import threading
# ---------------- #
except Exception as exception:
    # ---------------- #
    print(" - [ ERROR ] - LIBRARIES INITIALIZING ERROR.")
    exit(1)
# ---------------- #
try:
    # ---------------- #
    def JsonFilesLoader(FilePath):
        # ---------------- #
        try:
            # ---------------- #
            with open(FilePath, "r") as JsonFileObject:
                # ---------------- #
                return json.loads(JsonFileObject.read())
        # ---------------- # 
        except Exception as exception:
            # ---------------- #
            print(" - [ ERROR ] - JSON FILE LOADER ERROR.")
            exit(1)
    # ---------------- #
    def JsonFilesWriter(FilePath, data):
        # ---------------- #
        try:
            # ---------------- #
            with open(FilePath, "w") as JsonFileObject:
                # ---------------- #
                json.dump(data, JsonFileObject, indent=4, ensure_ascii=False)
                # ---------------- #
                return True
        # ---------------- # 
        except Exception as exception:
            # ---------------- #
            return False
            # ---------------- #
            print(" - [ ERROR ] - JSON FILE WRITER ERROR.")
            exit(1)
    # ---------------- #
    class LocalRequestsHandler():
        # ---------------- #
        def __init__(self):
            # ---------------- #
            try:
                # ---------------- #
                self.VariablesInitializing()
                self.LocalRequestsHandler()
            # ---------------- #
            except Exception as exception:
                # ---------------- #
                print(" - [ ERROR ] - LOCAL REQUESTS HANDLER LOADING ERROR.")
                exit(1)
        # ---------------- #
        def VariablesInitializing(self):
            # ---------------- #
            try:
                # ---------------- #
                self.LocalRequestsHandlerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.LocalRequestsHandlerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.LocalRequestsHandlerSocket.bind((socket.gethostname(), 1024))
                self.LocalRequestsHandlerSocket.listen(1)
            # ---------------- #
            except Exception as exception:
                # ---------------- #
                print(" - [ ERROR ] - VARIABLES INITIALIZING ERROR.")
                exit(1)
        # ---------------- #
        def LocalRequestsHandler(self):
            # ---------------- #
            try:
                # ---------------- #
                while True:
                    # ---------------- #
                    connection, address = self.LocalRequestsHandlerSocket.accept()
                    
                    # ---------------- #
                    RequestLength = int(connection.recv(8).decode("utf-8"))
                    RequestData = connection.recv(RequestLength).decode("utf-8")
                    RequestData = json.loads(RequestData)
                    # ---------------- #
                    RequestType, RequestData = RequestData[0], RequestData[1]
                    # ---------------- #
                    if RequestType == "GetOrderInfo":
                        # ---------------- #
                        OrdersDatabaseObject = JsonFilesLoader("OrdersDatabaseFile.json")
                        # ---------------- #
                        for i in OrdersDatabaseObject:
                            # ---------------- #
                            if i["OrderId"] == RequestData["OrderId"]:
                                # ---------------- #
                                RequestAnswer = i
                                # ---------------- #
                                RequestAnswer["OrderItemsInfo"] = dict()
                                # ---------------- #
                                ItemsDatabaseObject = JsonFilesLoader("ItemsDatabaseFile.json")[0]
                                # ---------------- #
                                for i in RequestAnswer["OrderItems"].keys():
                                    # ---------------- #
                                    if i in ItemsDatabaseObject:
                                        # ---------------- #
                                        RequestAnswer["OrderItemsInfo"][i] = ItemsDatabaseObject[i]
                                    # ---------------- #
                                    else:
                                        # ---------------- #
                                        RequestAnswer["OrderItemsInfo"][i] = "ERROR 404: ITEM NOT FOUND."
                                # ---------------- #
                                connection.send(bytes(str(len(str(RequestAnswer))), encoding="utf-8"))
                                connection.send(bytes(str(RequestAnswer), encoding="utf-8"))
                                # ---------------- #
                                break
                        # ---------------- #
                        else:
                            # ---------------- #
                            ErrorMessage = "CODE 404: NOT FOUND."
                            connection.send(bytes(str(len(ErrorMessage)), encoding="utf-8"))
                            connection.send(bytes(ErrorMessage, encoding="utf-8"))
                            # ---------------- #
                            connection.close()
                            # ---------------- #
                            continue
                    # ---------------- #
                    elif RequestType == "UpdateSubmission":
                        # ---------------- #
                        OrdersDatabaseObject = JsonFilesLoader("OrdersDatabaseFile.json")
                        # ---------------- #
                        for i in OrdersDatabaseObject:
                            # ---------------- #
                            if i["OrderId"] == RequestData["OrderId"]:
                                # ---------------- #
                                try:
                                    # ---------------- #
                                    for j in RequestData["OrderItems"]:
                                        # ---------------- #
                                        if j in i["OrderItems"].keys() and i["OrderItems"][j] == "delivered":
                                            # ---------------- #
                                            i["OrderItems"][j] = "submitted"
                                    # ---------------- #
                                    if JsonFilesWriter("OrdersDatabaseFile.json", OrdersDatabaseObject) == True:
                                        # ---------------- #
                                        connection.send(bytes("CODE 200: OK.", encoding="utf-8"))
                                    # ---------------- #
                                    else:
                                        # ---------------- #
                                        connection.send(bytes("CODE 501 : NOT IMPLEMENTED.", encoding="utf-8"))
                                # ---------------- #
                                except Exception as exception:
                                    # ---------------- #
                                    connection.send(bytes("CODE 501 : NOT IMPLEMENTED.", encoding="utf-8"))
                                # ---------------- #
                                break
                        # ---------------- #
                        else:
                            # ---------------- #
                            ErrorMessage = "CODE 404: NOT FOUND."
                            connection.send(bytes(str(len(ErrorMessage)), encoding="utf-8"))
                            connection.send(bytes(ErrorMessage, encoding="utf-8"))
                            # ---------------- #
                            connection.close()
                            # ---------------- #
                            continue
                    # ---------------- #
                    elif RequestType == "UpdateReturn":
                        # ---------------- #
                        OrdersDatabaseObject = JsonFilesLoader("OrdersDatabaseFile.json")
                        # ---------------- #
                        for i in OrdersDatabaseObject:
                            # ---------------- #
                            if i["OrderId"] == RequestData["OrderId"]:
                                # ---------------- #
                                try:
                                    # ---------------- #
                                    for j in RequestData["OrderItems"]:
                                        # ---------------- #
                                        if j in i["OrderItems"].keys() and i["OrderItems"][j] == "submitted":
                                            # ---------------- #
                                            i["OrderItems"][j] = "returned"
                                        # ---------------- #
                                        else:
                                            # ---------------- #
                                            connection.send(bytes("CODE 501: YOU CAN'T RETURN SOME OF ITEMS."))
                                            # ---------------- #
                                            break
                                    # ---------------- #
                                    else:
                                        # ---------------- #
                                        if JsonFilesWriter("OrdersDatabaseFile.json", OrdersDatabaseObject) == True:
                                            # ---------------- #
                                            connection.send(bytes("CODE 200: OK.", encoding="utf-8"))
                                        # ---------------- #
                                        else:
                                            # ---------------- #
                                            connection.send(bytes("CODE 501 : NOT IMPLEMENTED.", encoding="utf-8"))
                                # ---------------- #
                                except Exception as exception:
                                    # ---------------- #
                                    connection.send(bytes("CODE 501 : NOT IMPLEMENTED.", encoding="utf-8"))
                                # ---------------- #
                                break
                        # ---------------- #
                        else:
                            # ---------------- #
                            ErrorMessage = "CODE 404: NOT FOUND."
                            connection.send(bytes(str(len(ErrorMessage)), encoding="utf-8"))
                            connection.send(bytes(ErrorMessage, encoding="utf-8"))
                            # ---------------- #
                            connection.close()
                            # ---------------- #
                            continue
            # ---------------- #
            except Exception as exception:
                # ---------------- #
                print(" - [ ERROR ] - LOCAL REQUESTS HANDLER ERROR.")
                # exit(1)
            # ---------------- #
            finally:
                # ---------------- #
                self.LocalRequestsHandlerSocket.close()
# ---------------- #
except Exception as exception:
    # ---------------- #
    print(" - [ ERROR ] - CLASSES INITIALIZING ERROR.")
    exit(1)
# ---------------- #
try:
    # ---------------- #
    if __name__ == "__main__":
        # ---------------- #
        LocalRequestsHandlerThread = threading.Thread(target=LocalRequestsHandler)
        # ---------------- #
        LocalRequestsHandlerThread.start()
        # ---------------- #
        LocalRequestsHandlerThread.join()
# ---------------- #
except Exception as exception:
    # ---------------- #
    print(" - [ ERROR ] - PROGRAMME STARTING ERROR.")
    exit(1)
    # ---------------- #