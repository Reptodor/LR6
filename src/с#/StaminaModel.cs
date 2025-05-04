using System;

public class StaminaModel
{
    private readonly float _redPercentage = 0.2f;
    private readonly float _baseValue;

    private float _currentValue;
    private bool _isEmpty;

    private float _currentPercentage => _currentValue / _baseValue;

    public event Action<float> ValueChanged;

    public StaminaModel(float baseStamina)
    {
        _baseValue = baseStamina;
        _currentValue = _baseValue;
    }

    public bool CanUse()
    {
        if(_currentPercentage > _redPercentage)
            _isEmpty = false;

        if(_currentPercentage <= _redPercentage && _isEmpty)
            return false;

        return true;
    }

    public void Increase(float increaseAmount)
    {
        if(increaseAmount < 0)
            throw new ArgumentOutOfRangeException(nameof(increaseAmount), "Increase amount must be greater or equals zero");

        if(_currentValue >= _baseValue)
            return;

        _currentValue += increaseAmount;

        ValueChanged?.Invoke(_currentPercentage);
    }

    public void Reduce(float reduceAmount)
    {
        if(reduceAmount < 0)
            throw new ArgumentOutOfRangeException(nameof(reduceAmount), "Reduce amount must be greater or equals zero");

        if(_currentValue <= 0)
            return;

        _currentValue -= reduceAmount;

        ValueChanged?.Invoke(_currentPercentage);

        if(_currentValue <= 0)
            _isEmpty = true;
    }
}
