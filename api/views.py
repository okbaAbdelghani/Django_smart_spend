from rest_framework import response , status
from rest_framework.decorators import api_view 
from base.models import Item, User, Account
from .serializers import ItemSerializer , UserSerializer, AccountSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return response.Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)

@api_view(['POST'])
def addUser(requst):
    serializer = UserSerializer(data=requst.data)
    if serializer.is_valid():
        serializer.save()
    return response.Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return response.Response(serializer.data)

@api_view(['POST'])
def addAccount(request, user_id):
    try:
        user_account = Account(user_id=user_id)
        serializer = AccountSerializer(user_account,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response.Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def getAccounts(request, user_id):
    try:
        accounts = Account.objects.filter(user_id=user_id)
        serializer = AccountSerializer(accounts, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return response.Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)